import sys  # Importa funcionalidades do sistema, necessário para sys.exit()
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
from tela import Ui_MainWindow  # Importa a interface gerada pelo Qt Designer

class GerenciadorTarefas(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicializa a janela principal da aplicação
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Monta os widgets da interface na janela

        # Criar lista de tarefas na interface
        self.lista = QListWidget(self)  # Cria o widget QListWidget
        self.lista.setGeometry(950, 90, 400, 650)  # Define posição e tamanho (x, y, largura, altura)
        self.lista.setObjectName("listaTarefas")  # Nome interno do widget (útil para estilos)

        # Estilo da lista
        self.lista.setStyleSheet("""
            QListWidget {
                font-size: 20px;              /* Tamanho da fonte do texto */
                color: black;                 /* Cor do texto */
                border: 2px solid blue;       /* Borda azul em volta da lista */
                border-radius: 5px;           /* Cantos levemente arredondados */
                background-color: white;      /* Cor de fundo da lista */
            }

            QListWidget::item {
                border-bottom: 1px solid #1e90ff;  /* Linha azul separando os itens */
                padding: 5px;                      /* Espaço interno em cada item */
            }

            QListWidget::item:last {
                border-bottom: none;               /* Remove a linha do último item */
            }

            QListWidget::item:selected {
                background-color: #3399ff;         /* Fundo azul quando item selecionado */
                color: white;                      /* Texto branco quando item selecionado */
            }
        """)

        # Conectar botões da interface aos métodos
        self.ui.Adicionar.clicked.connect(self.adicionar_tarefa)  # Botão Adicionar chama adicionar_tarefa
        self.ui.pushButton_2.clicked.connect(self.excluir_tarefa)  # Botão Excluir chama excluir_tarefa

    def adicionar_tarefa(self):
        titulo = self.ui.Titulo.text()  # Pega o texto digitado no campo Titulo
        descricao = self.ui.Descricao.toPlainText()  # Pega o texto digitado na área de Descricao

        if titulo:  # Só adiciona se houver um título
            item = QListWidgetItem(f"{titulo} - {descricao}")  # Cria um item com título e descrição
            self.lista.addItem(item)  # Adiciona o item à lista
            self.ui.Titulo.clear()  # Limpa o campo Titulo
            self.ui.Descricao.clear()  # Limpa o campo Descricao

    def excluir_tarefa(self):
        item = self.lista.currentRow()  # Pega o índice do item atualmente selecionado
        if item >= 0:  # Se houver um item selecionado
            self.lista.takeItem(item)  # Remove o item da lista

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Cria a aplicação
    janela = GerenciadorTarefas()  # Cria a janela principal
    janela.show()  # Exibe a janela na tela
    sys.exit(app.exec())  # Executa o loop principal da aplicação até o usuário fechar
