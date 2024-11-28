CC = $(shell command -v clang > /dev/null 2>&1 && echo clang || echo gcc)
CXX = $(shell command -v clang++ > /dev/null 2>&1 && echo clang++ || echo g++)
CXXFLAGS = -std=c++17 -lhpdf -lcryptopp
LIBS = `pkg-config --cflags --libs opencv4 eigen3`

all: gray2color.out PT2fisheye.out cubemap2fisheye.out change_index.out log2pdf.out encryptor.out VisionVoyageServer.out

%.out: %.cc
	$(CXX) $< -o $@ $(CXXFLAGS) $(LIBS)

VisionVoyageServer.out: VisionVoyageServer.c
	$(CC) $< -o $@

.PHONY: all clean

clean:
	rm -f *.out

