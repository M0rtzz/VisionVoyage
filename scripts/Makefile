CC = g++
CXXFLAGS = -std=c++17
LIBS = `pkg-config --cflags --libs opencv4 eigen3`

all: gray2color.out PT2fisheye.out cubemap2fisheye.out VisionVoyageServer.out

gray2color.out: gray2color.cc
	$(CC) $(CXXFLAGS) $< -o $@ $(LIBS)

PT2fisheye.out: PT2fisheye.cc
	$(CC) $(CXXFLAGS) $< -o $@ $(LIBS)

cubemap2fisheye.out: cubemap2fisheye.cc
	$(CC) $(CXXFLAGS) $< -o $@ $(LIBS)

VisionVoyageServer.out: VisionVoyageServer.c
	gcc $< -o $@

.PHONY: clean
clean:
	rm -f gray2color.out PT2fisheye.out cubemap2fisheye.out VisionVoyageServer.out

