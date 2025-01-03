from PIL import Image, ImageTk
from alipay import AliPay
from io import BytesIO
import tkinter as tk
import numpy as np
import threading
import datetime
import requests
import qrcode
import time
import cv2
import os


class AlipayPayment:
    def __init__(self, app_private_key_path, alipay_public_key_path):
        self.app_private_key_string = open(app_private_key_path).read()
        self.alipay_public_key_string = open(alipay_public_key_path).read()
        self.alipay = AliPay(
            appid="2021004163658784",
            app_notify_url=None,
            app_private_key_string=self.app_private_key_string,
            alipay_public_key_string=self.alipay_public_key_string,
            sign_type="RSA2",
            debug=False
        )

    def createOrder(self):
        out_trade_no = "VisionVoyage"
        current_time = datetime.datetime.now().strftime("Year:%Y_Month:%m_Day:%d_%H:%M:%S")
        out_trade_no_with_time = out_trade_no + "_" + current_time
        # BUG: ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        result = self.alipay.api_alipay_trade_precreate(
            subject="Upgrade to VisionVoyage Plus",
            out_trade_no=out_trade_no_with_time,
            total_amount=1
        )
        print(result)
        qr_code_url = result.get('qr_code')
        return qr_code_url, out_trade_no_with_time

    def generateQrCode(self, qr_code_url):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_code_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        qr_pil = img.convert('RGB')
        qr_cv = cv2.cvtColor(np.array(qr_pil), cv2.COLOR_RGB2BGR)
        return qr_cv

    def displayQrCodeOnBackground(self, qr_cv, background_url):

        def showImage(background, title):
            root = tk.Tk()
            root.title(title)
            photo = ImageTk.PhotoImage(background)
            label = tk.Label(image=photo)
            label.image = photo
            label.pack()
            root.mainloop()

        def processImage(qr_image, background, title):
            qr_width, qr_height = qr_image.size
            bg_width, bg_height = background.size
            center_x = int(bg_width / 2)
            center_y = int((336 + 738) / 2)
            qr_x = center_x - int(qr_width / 2)
            qr_y = center_y - int(qr_height / 2)
            background.paste(qr_image, (qr_x, qr_y))

            # 在主线程中显示图像
            showImage(background, title)

        qr_image = Image.fromarray(cv2.cvtColor(qr_cv, cv2.COLOR_BGR2RGB)).convert("RGB")

        response = requests.get(background_url)
        background_bytes = BytesIO(response.content)
        background = Image.open(background_bytes)
        title = "请在三分钟内完成支付"
        threading.Thread(target=processImage, args=(qr_image, background, title)).start()

    def checkPaymentStatus(self, out_trade_no_with_time, phone_number):
        paid = False
        for i in range(36):
            result = self.alipay.api_alipay_trade_query(out_trade_no=out_trade_no_with_time)
            # WAIT_BUYER_PAY
            if result.get("trade_status", "") == "TRADE_SUCCESS":
                '''如：
                {'code': '10000', 'msg': 'Success', 'buyer_logon_id': '150******10', 'buyer_pay_amount': '1.00', 'fund_bill_list': [{'amount': '1.00', 'fund_channel': 'ALIPAYACCOUNT'}], 'invoice_amount': '1.00', 'out_trade_no': 'VisionVoyage_Year:2024_Month:03_Day:16_20:49:33', 'point_amount': '0.00', 'receipt_amount': '1.00', 'send_pay_date': '2024-03-16 20:50:15', 'total_amount': '1.00', 'trade_no': '2024031622001477011405355171', 'trade_status': 'TRADE_SUCCESS', 'buyer_open_id': '001OBDctSn0Cp6XAHwAJOSX86oRFK5giogmBm_OVwrOJvoe'}
                '''
                print(result)
                # buyer_logon_id = result.get("buyer_logon_id")
                buyer_logon_id = phone_number
                trade_no = result.get("trade_no")
                trade_status = result.get("trade_status")
                buyer_open_id = result.get("buyer_open_id")
                terminal_command = "./scripts/encryptor.out true " + buyer_logon_id + \
                    " " + trade_no + " " + trade_status + " " + buyer_open_id
                os.system(terminal_command)
                paid = True
                # break
                print("\033[1;32mPayment successful!\033[0m")
                return paid
            time.sleep(5)
            print("\033[1;31mPayment not yet completed ...\033[0m")

        if paid is False:
            print("\033[1;31mPayment failed, canceling the order\033[0m")
            buyer_logon_id = phone_number
            trade_no = 'NONE'
            trade_status = 'TRADE_FAILURE'
            buyer_open_id = 'NONE'
            terminal_command = "./scripts/encryptor.out true " + buyer_logon_id + \
                " " + trade_no + " " + trade_status + " " + buyer_open_id
            os.system(terminal_command)
            self.alipay.api_alipay_trade_cancel(out_trade_no=out_trade_no_with_time)

        return paid
