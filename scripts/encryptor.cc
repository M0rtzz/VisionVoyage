#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <cryptopp/aes.h>
#include <cryptopp/modes.h>
#include <cryptopp/filters.h>
#include <cryptopp/files.h>
#include <cryptopp/base64.h>
#include <cryptopp/osrng.h>

class EncryptionHelper
{
public:
    void encryptData(const std::string &data, const std::string &key, const std::string &iv, const std::string &output_file)
    {
        // 生成AES加密所需的密钥和初始化向量
        byte aesKey[CryptoPP::AES::DEFAULT_KEYLENGTH];
        byte aesIV[CryptoPP::AES::BLOCKSIZE];

        CryptoPP::StringSource(key, true, new CryptoPP::ArraySink(aesKey, CryptoPP::AES::DEFAULT_KEYLENGTH));
        CryptoPP::StringSource(iv, true, new CryptoPP::ArraySink(aesIV, CryptoPP::AES::BLOCKSIZE));

        // 创建AES加密对象
        CryptoPP::CBC_Mode<CryptoPP::AES>::Encryption encryption(aesKey, CryptoPP::AES::DEFAULT_KEYLENGTH, aesIV);

        // 将数据进行加密
        std::string encrypted;
        CryptoPP::StringSource(data, true, new CryptoPP::StreamTransformationFilter(encryption, new CryptoPP::StringSink(encrypted)));

        // 将加密后的数据写入文件
        std::ofstream file(output_file.c_str(), std::ios::binary | std::ios::trunc);
        file.write(encrypted.data(), encrypted.size());
    }

    std::string decryptData(const std::string &inputFile, const std::string &key, const std::string &iv)
    {
        // 生成AES解密所需的密钥和初始化向量
        byte aesKey[CryptoPP::AES::DEFAULT_KEYLENGTH];
        byte aesIV[CryptoPP::AES::BLOCKSIZE];

        CryptoPP::StringSource(key, true, new CryptoPP::ArraySink(aesKey, CryptoPP::AES::DEFAULT_KEYLENGTH));
        CryptoPP::StringSource(iv, true, new CryptoPP::ArraySink(aesIV, CryptoPP::AES::BLOCKSIZE));

        // 创建AES解密对象
        CryptoPP::CBC_Mode<CryptoPP::AES>::Decryption decryption(aesKey, CryptoPP::AES::DEFAULT_KEYLENGTH, aesIV);

        // 从文件中读取加密数据
        std::ifstream file(inputFile.c_str(), std::ios::binary);
        std::string encrypted((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

        // 对数据进行解密
        std::string decrypted;
        CryptoPP::StringSource(encrypted, true, new CryptoPP::StreamTransformationFilter(decryption, new CryptoPP::StringSink(decrypted)));

        return decrypted;
    }
};

int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        // std::cerr << "Usage: at least: is_encrypt buyer_logon_id or more." << std::endl;
        return EXIT_FAILURE;
    }

    std::string trade_no = "";
    std::string trade_status = "";
    std::string buyer_open_id = "";

    std::string is_encrypt = argv[1];
    std::string buyer_logon_id = argv[2];
    std::transform(is_encrypt.begin(), is_encrypt.end(), is_encrypt.begin(), ::tolower);
    bool is_encrypt_bool = (is_encrypt == "true");
    if (is_encrypt_bool)
    {
        trade_no = argv[3];
        trade_status = argv[4];
        buyer_open_id = argv[5];
    }

    // std::string cleaned_logon_id = "";
    // for (char c : buyer_logon_id)
    // {
    //     if (c != '*')
    //     {
    //         cleaned_logon_id += c;
    //     }

    // }
    // std::string data2process = cleaned_logon_id + "," + trade_no + "," + trade_status + "," + buyer_open_id;

    std::string data2process = buyer_logon_id + "," + trade_no + "," + trade_status + "," + buyer_open_id;
    std::string key = "M0rtzzAshore!!!!";                               // 替换为您的密钥
    std::string iv = "M0rtzzGod!!!!!!!";                                // 替换为您的初始化向量
    std::string output_file = "./private/" + buyer_logon_id + ".enc";   // 保存加密数据的文件名

    EncryptionHelper helper;

    if (is_encrypt_bool)
    {
        helper.encryptData(data2process, key, iv, output_file);
        std::cout << "Data encrypted and saved to file: " << output_file << std::endl;
    }
    else
    {
        std::string decrypted_data = helper.decryptData(output_file, key, iv);
        std::cout << "Decrypted data: " << decrypted_data << std::endl;
    }

    return EXIT_SUCCESS;
}
