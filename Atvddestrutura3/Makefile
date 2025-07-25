# Makefile para compilar
CXX = g++
CXXFLAGS = -Wall -std=c++17

TARGET = lista
OBJS = main.cpp

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

clean:
	rm -f $(TARGET)
