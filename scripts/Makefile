CC = g++
CXXFLAGS = -std=c++17 -lhpdf -lcryptopp
LIBS = `pkg-config --cflags --libs opencv4 eigen3`

all: gray2color.out PT2fisheye.out cubemap2fisheye.out change_index.out txt2pdf.out encryptor.out VisionVoyageServer.out

%.out: %.cc
	$(CC) $< -o $@ $(CXXFLAGS) $(LIBS)

VisionVoyageServer.out: VisionVoyageServer.c
	gcc $< -o $@

.PHONY: clean
clean:
	rm -f *.out

