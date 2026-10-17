# TaskTracker — Fase 2
Aplicação CLI de Guilherme Fernades Monteiro (RA 22403229) em Python 3.11+.
## Instalação e execução
Sem dependências externas. Na raiz do repositório:
```sh
python3 src/main.py
```
O menu oferece cadastro (1), listagem (2), saída (3) e conclusão (4).
A opção 4 preserva o algoritmo da Fase 1 sem renumerar o menu obrigatório da Fase 2.
Título vazio e prioridade fora de Alta/Média/Media/Baixa são rejeitados com nova pergunta.
O prazo exige DD/MM/AAAA e não pode ser passado, conforme o planejamento inicial.
As tarefas são dicionários em uma lista em memória; encerrar elimina os dados.
A listagem mostra todos os campos, ID, agrupamento por status e totais.
## Estrutura
- src/main.py: menu, operações e validações.
- docs/planejamento_logico.pdf: conversão integral do documento da Fase 1.
- docs/*.docx: original preservado.
- .gitignore: caches e ambientes virtuais.
## Validação
Ver ../evidencias/tasktracker_terminal.txt e ../RELATORIO_VALIDACAO.md.
## Próxima fase
Empacotamento, testes e Docker; esta entrega não afirma deploy ou containerização.
