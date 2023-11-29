CC = g++
CFLAGS = -std=c++17
LIBS = `pkg-config --cflags --libs opencv4`

all: gray2color change_index rename2random check_if_six_figures

gray2color: gray2color.cc
	$(CC) $(CFLAGS) $< -o $@ $(LIBS)

change_index: change_index.cc
	$(CC) $(CFLAGS) $< -o $@ $(LIBS)

rename2random: rename2random.cc
	$(CC) $(CFLAGS) $< -o $@

check_if_six_figures: check_if_six_figures.cc
	$(CC) $(CFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -f gray2color change_index rename2random check_if_six_figures

