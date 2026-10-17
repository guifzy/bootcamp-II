"""TaskTracker: cadastro, consulta e conclusão de tarefas em memória."""
from datetime import date, datetime
from collections.abc import Callable


def criar_tarefa(titulo: str, descricao: str, prioridade: str, prazo: str) -> dict[str, str]:
    """Valida uma tarefa antes de adicioná-la à lista."""
    if not titulo.strip():
        raise ValueError("O título não pode ficar vazio.")
    if prioridade not in {"Alta", "Média", "Media", "Baixa"}:
        raise ValueError("Prioridade inválida. Use Alta, Média (ou Media) ou Baixa.")
    try:
        limite = datetime.strptime(prazo, "%d/%m/%Y").date()
        if limite.strftime("%d/%m/%Y") != prazo:
            raise ValueError("Formato de data inválido")
    except ValueError as exc:
        raise ValueError("Data inválida. Use DD/MM/AAAA.") from exc
    if limite < date.today():
        raise ValueError("A data limite não pode ser anterior a hoje.")
    return {"titulo": titulo.strip(), "descricao": descricao.strip(),
            "prioridade": "Média" if prioridade == "Media" else prioridade,
            "data_limite": limite.strftime("%d/%m/%Y"), "status": "Pendente"}


def pedir(mensagem: str, validar: Callable[[str], None]) -> str:
    """Repete a pergunta até receber um valor válido."""
    while True:
        valor = input(mensagem)
        try:
            validar(valor)
            return valor
        except ValueError as exc:
            print(exc)


def validar_titulo(valor: str) -> None:
    """Rejeita um título vazio ou com espaços."""
    if not valor.strip():
        raise ValueError("O título não pode ficar vazio.")


def validar_prioridade(valor: str) -> None:
    """Exige uma das grafias autorizadas no enunciado."""
    if valor not in {"Alta", "Média", "Media", "Baixa"}:
        raise ValueError("Prioridade inválida. Use Alta, Média (ou Media) ou Baixa.")


def validar_data(valor: str) -> None:
    """Aplica a validação de prazo definida na Fase 1."""
    criar_tarefa("Validação", "", "Baixa", valor)


def cadastrar(tarefas: list[dict[str, str]]) -> None:
    """Coleta entradas válidas e registra uma tarefa pendente."""
    titulo = pedir("Título: ", validar_titulo)
    descricao = input("Descrição: ")
    prioridade = pedir("Prioridade (Alta/Média/Media/Baixa): ", validar_prioridade)
    prazo = pedir("Data limite (DD/MM/AAAA): ", validar_data)
    tarefas.append(criar_tarefa(titulo, descricao, prioridade, prazo))
    print("Tarefa cadastrada com sucesso!")


def listar(tarefas: list[dict[str, str]]) -> None:
    """Exibe todas as propriedades, por status, e o resumo."""
    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return
    for status in ("Pendente", "Concluída"):
        print(f"\n{status}:")
        for numero, tarefa in enumerate(tarefas, 1):
            if tarefa["status"] == status:
                print(f"ID: {numero}")
                for campo, valor in tarefa.items():
                    print(f"  {campo}: {valor}")
    concluidas = sum(t["status"] == "Concluída" for t in tarefas)
    print(f"Total: {len(tarefas)} | Concluídas: {concluidas}")


def concluir(tarefas: list[dict[str, str]]) -> None:
    """Conclui uma tarefa existente pelo identificador mostrado na lista."""
    try:
        numero = int(input("ID da tarefa: "))
        if not 1 <= numero <= len(tarefas):
            raise ValueError
    except ValueError:
        print("Tarefa não encontrada. Informe um ID existente.")
        return
    tarefas[numero - 1]["status"] = "Concluída"
    print("Tarefa concluída com sucesso!")


def main() -> None:
    """Executa o menu contínuo; os dados duram apenas esta sessão."""
    tarefas: list[dict[str, str]] = []
    while True:
        print(f"\nTaskTracker — {len(tarefas)} tarefa(s) nesta sessão")
        print("\n1. Cadastrar nova tarefa\n2. Visualizar tarefas cadastradas"
              "\n3. Sair da aplicação\n4. Concluir tarefa")
        try:
            opcao = input("Opção: ").strip()
            if opcao == "1":
                cadastrar(tarefas)
            elif opcao == "2":
                listar(tarefas)
            elif opcao == "3":
                print("Aplicação encerrada.")
                break
            elif opcao == "4":
                concluir(tarefas)
            else:
                print("Opção inválida. Escolha 1, 2, 3 ou 4.")
        except (EOFError, KeyboardInterrupt):
            print("\nAplicação encerrada.")
            break


if __name__ == "__main__":
    main()
