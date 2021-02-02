#!/usr/bin/env python
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        geckodriver_path = os.path.join(os.getcwd(), '..', 'geckodriver')
        ff_options = Options()
        ff_options.add_argument('--headless')

        self.browser = webdriver.Firefox(
            executable_path=geckodriver_path,
            options=ff_options
        )

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith ouviu falar de uma nova aplicação online interessante
        # para lista de tarefas. Ele decidiu verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebeu que o título da página e o cabeçalho
        # mencionam listas de tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # Ela é convidada a insetir um item de tarefa imediatamente

        # Ela digita "Comprar penas de pavão" em uma caixa de texto
        # (o hobby de Edith é fazer iscas para pescas com penas)

        # Quando ela tecla "enter", a página é atualizada, e agora
        # a página lista "1: Comprar penas de pavão" como um item
        # em uma lista de tarefas

        # Ainda continua havendo uma caixa de texto convidando-a a
        # acrescentar outro item. Ela insere "Usar penas de pavão
        # para fazer uma isca" - Edith é bem metódica)

        # A página é atualizada novamente e agora mostra os dois
        # itens em sua lista

        # Edith se pergunta se o site lembrará de sua lista. Então
        # ela nota que o site gerou um URL único para ela -- há um
        # pequeno texto explicativo para isso

        # Ela acessa esse URL - sua lista de tarefas continua lá

        # Satisfeita, ela volta a dormir


if __name__ == '__main__':
    unittest.main()
