# Define as perguntas disponíveis e suas respostas
questions = {
    1: "O que é a Plataforma ESG?",
    2: "Quais são os objetivos da Plataforma ESG?",
    3: "Como posso me cadastrar na plataforma?",
    4: "Quais são os benefícios de usar a Plataforma ESG?",
    5: "Como posso encontrar empresas que adotam práticas ESG?",
    6: "Quais são as principais funcionalidades da plataforma?",
    7: "Como posso contribuir para a comunidade da Plataforma ESG?",
    8: "É possível compartilhar conteúdo na plataforma?",
    9: "Quais são os princípios ESG e por que são importantes?",
    10: "Como posso aprender mais sobre práticas sustentáveis?",
    11: "A Plataforma ESG oferece recursos educacionais sobre sustentabilidade?",
    12: "Como faço para relatar um problema técnico na plataforma?",
    13: "Quem devo contatar em caso de dificuldades de acesso à minha conta?",
    14: "Existe algum canal de suporte técnico disponível fora da plataforma?",
    15: "Como a Plataforma ESG protege minhas informações pessoais?",
    16: "Quais são as políticas de privacidade e segurança da plataforma?",
    17: "Onde posso encontrar informações sobre a segurança dos meus dados na plataforma?"
}

# Define as respostas correspondentes às perguntas
answers = {
    1: "A Plataforma ESG é uma rede social que promove práticas sustentáveis e responsabilidade social.",
    2: "Os principais objetivos da Plataforma ESG são incentivar a adoção de práticas ESG, promover a conscientização sobre sustentabilidade e conectar pessoas e empresas comprometidas com esses valores.",
    3: "Você pode se cadastrar na Plataforma ESG preenchendo o formulário de cadastro disponível na página inicial.",
    4: "Os benefícios de usar a Plataforma ESG incluem acesso a conteúdo relevante sobre sustentabilidade, oportunidades de networking com indivíduos e empresas alinhadas com os princípios ESG e a possibilidade de contribuir para um futuro mais sustentável.",
    5: "Você pode encontrar empresas que adotam práticas ESG usando a função de pesquisa na plataforma ou explorando os grupos de interesse relacionados.",
    6: "As principais funcionalidades da Plataforma ESG incluem feeds de notícias personalizados, fóruns de discussão, grupos de interesse, calendário de eventos e a capacidade de compartilhar conteúdo relacionado à sustentabilidade.",
    7: "Você pode contribuir para a comunidade da Plataforma ESG compartilhando conteúdo relevante, participando de discussões nos fóruns e grupos de interesse, e participando de eventos e campanhas relacionadas aos ODS.",
    8: "Sim, é possível compartilhar conteúdo na Plataforma ESG. Você pode postar artigos, vídeos, fotos e outros materiais relacionados a práticas sustentáveis e responsabilidade social.",
    9: "Os princípios ESG referem-se a critérios ambientais, sociais e de governança que as empresas devem considerar em suas operações. Eles são importantes porque ajudam a promover práticas empresariais sustentáveis, responsáveis e éticas.",
    10: "Você pode aprender mais sobre práticas sustentáveis explorando o conteúdo educacional disponível na Plataforma ESG, participando de eventos e workshops, e interagindo com outros membros da comunidade comprometidos com a sustentabilidade.",
    11: "Sim, a Plataforma ESG oferece uma variedade de recursos educacionais, incluindo artigos, vídeos, webinars e cursos online sobre sustentabilidade e responsabilidade social.",
    12: "Você pode relatar um problema técnico na Plataforma ESG entrando em contato com nossa equipe de suporte técnico através do formulário de contato disponível na plataforma ou enviando um e-mail para support@esgplatform.com.",
    13: "Em caso de dificuldades de acesso à sua conta, entre em contato com nossa equipe de suporte técnico através do formulário de contato disponível na plataforma ou enviando um e-mail para support@esgplatform.com.",
    14: "Sim, você pode entrar em contato com nosso suporte técnico enviando um e-mail para support@esgplatform.com ou ligando para o número +1 (123) 456-7890.",
    15: "A Plataforma ESG protege suas informações pessoais utilizando medidas de segurança robustas, como criptografia de dados e acesso restrito aos dados do usuário.",
    16: "Nossas políticas de privacidade e segurança estão detalhadas em nossos Termos de Serviço e Política de Privacidade, disponíveis na plataforma.",
    17: "Você pode encontrar informações detalhadas sobre a segurança dos seus dados na seção 'Segurança e Privacidade' do nosso site ou entrando em contato com nossa equipe de suporte técnico."
}

# Função para interagir com o chatbot
def chat():
    print("Bem-vindo ao Chatbot da Plataforma ESG!")
    print("Por favor, escolha o número correspondente à pergunta que você gostaria de fazer:")
    print("")

    while True:
        # Exibir lista de perguntas
        for num, question in questions.items():
            print(f"{num}: {question}")

        print("")

        # Solicitar ao usuário que escolha uma pergunta
        user_choice = int(input("Escolha o número da pergunta que deseja fazer: "))

        # Verificar se a escolha do usuário é válida
        if user_choice not in questions.keys():
            print("Opção inválida. Por favor, escolha um número válido.")
            continue

        # Obter e exibir resposta correspondente à pergunta escolhida
        print("")
        print("Resposta: " + answers[user_choice])
        print("")

        # Perguntar ao usuário se ele deseja fazer outra pergunta
        again = input("Gostaria de fazer outra pergunta? (sim/não): ")
        if again.lower() != "sim":
            print("Chat encerrado. Obrigado por utilizar o Chatbot da Plataforma ESG!")
            break

# Iniciar o chatbot
chat()