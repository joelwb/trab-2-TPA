# Trabalho 2 - Técnicas Avançadas de Programação

Neste diretório encontram-se os arquivos para entrega do segundo trabalho de TPA, contendo um arquivo do relatório em código fonte LaTeX, o arquivo do relatório em PDF, e os códigos fontes com as funções principais e os algoritmos de ordenação na pasta.

Os algoritmos deste trabalho foram desenvolvidos na linguagem Python 3.7, no sistema operacional Windows 10. Para executar nosso código fonte não é necessário compilação. Para executar o código fonte é necessário passar 3 parâmetros para a função main.py. Os parâmetros são os seguintes: 
- -i: diretório do arquivo de entrada;
- -o: diretório do arquivo de saída;
- -a: algoritmo de ordenação a ser executado. O nome do algoritmo de ordenação deve ser passado como a seguir:
	- quick_sort
	- merge_sort
	- heap_sort
	- insertion_sort
	- selection_sort
	- intro_sort
	- tim_sort

Portanto, para executar o código fonte basta apenas utilizar o seguinte comando no terminal dentro do diretório onde se encontram os códigos fonte:

Linux/GNU: <br>
`python3 main.py -a algoritmo -i input_file.csv -o outputfile.csv`

Windows:<br>
`py main.py -a algoritmo -i input_file.csv -o outputfile.csv`

## Grupo
- André Martins
- Joel Belmiro
- Nicolas Sampaio