CC = g++
CXXFLAGS = -std=c++17
LIBS = `pkg-config --cflags --libs opencv4 eigen3`

all: gray2color PT2fisheye cubemap2fisheye VisionVoyageServer

gray2color: gray2color.cc
	$(CC) $(CFLAGS) $< -o $@ $(LIBS)

PT2fisheye: PT2fisheye.cc
	$(CC) $(CFLAGS) $< -o $@ $(LIBS)

cubemap2fisheye: cubemap2fisheye.cc
	$(CC) $(CFLAGS) $< -o $@ $(LIBS)

VisionVoyageServer: VisionVoyageServer.c
	gcc $< -o $@

.PHONY: clean
clean:
	rm -f gray2color PT2fisheye cubemap2fisheye VisionVoyageServer

