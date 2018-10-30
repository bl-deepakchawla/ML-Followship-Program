import textwrap


def formatted_text(l_text_value):
    print(textwrap.fill(l_text_value, width=50))


g_text_value = '''
      Machine learning is an application of artificial intelligence (AI) that provides systems the ability to 
      automatically learn and improve from experience without being explicitly programmed. Machine learning 
      focuses on the development of computer programs that can access data and use it learn for themselves..
      '''
formatted_text(g_text_value)
