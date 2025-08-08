# Define o compilador C++ a ser usado
CXX = g++

# Define as flags do compilador (por exemplo, -Wall para todos os avisos)
CXXFLAGS = -Wall -std=c++11

# Define o nome do executável final
TARGET = meu_programa_fila

# Define os arquivos objeto que serão gerados
OBJS = FilaSequencial.o main.o

# Regra padrão: compila o programa
all: $(TARGET)

# Regra para criar o executável a partir dos arquivos objeto
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(TARGET)

# Regra para compilar FilaSequencial.cpp em FilaSequencial.o
FilaSequencial.o: FilaSequencial.cpp FilaSequencial.h
	$(CXX) $(CXXFLAGS) -c FilaSequencial.cpp

# Regra para compilar main.cpp em main.o
main.o: main.cpp FilaSequencial.h
	$(CXX) $(CXXFLAGS) -c main.cpp

# Regra para limpar os arquivos gerados (objetos e executável)
clean:
	rm -f $(OBJS) $(TARGET)
