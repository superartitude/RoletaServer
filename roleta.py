from time import sleep as sl
from random import choice, randint
import requests
import os
import sys
import discord
from discord.ext import commands
import os
import sys
from random import choice, randint
from flask import Flask
from threading import Thread





diretorio_mestre = os.path.dirname(os.path.abspath(sys.argv[0]))
#importações
def chamar_racas():
    caminho = os.path.join(diretorio_mestre, 'racas.txt')
    with open(caminho,'r', encoding='utf-8') as arquivo:
        lista = arquivo.read().splitlines()
    return lista

todas_as_racas = chamar_racas()
def chamar_armas():
    caminho = os.path.join(diretorio_mestre,'Armas.txt')
    with open(caminho,'r',encoding='utf-8') as arquivo:
        lista = arquivo.read().splitlines()
    return lista

todas_as_armas = chamar_armas()
def chamar_classes():
    caminho = os.path.join(diretorio_mestre,'Classes.txt')
    with open(caminho,'r',encoding='utf-8') as arquivo:
        lista = arquivo.read().splitlines()
    return lista

todas_as_Classes = chamar_classes()
def chamar_mundos():
    caminho = os.path.join(diretorio_mestre,'Mundos.txt')
    with open(caminho,'r',encoding='utf-8') as arquivo:
        lista = arquivo.read().splitlines()
    return lista

todos_os_mundos = chamar_mundos()
def chamar_fraquezas():
    caminho = os.path.join(diretorio_mestre,'fraquezas.txt')
    with open(caminho,'r', encoding='utf-8') as arquivo:
        lista = arquivo.read().splitlines()
    return lista

todas_as_fraquezas = chamar_fraquezas()
def chamar_missao():
    caminho = os.path.join(diretorio_mestre,'Missao.txt')
    with open(caminho,'r',encoding='utf-8') as arquivo:
        lista = arquivo.read().splitlines()
    return lista

todas_as_missoes = chamar_missao()
def chamar_habil():
    caminho = os.path.join(diretorio_mestre,'habilidades.txt')
    with open(caminho,'r',encoding='utf-8') as arquivo:
        lista = arquivo.read().splitlines()
    return lista

todas_as_habil = chamar_habil()
def chamar_alinhamento():
    caminho = os.path.join(diretorio_mestre,'Alinhamentos.txt')
    with open(caminho,'r',encoding='utf-8') as arquivo:
        lista = arquivo.read().splitlines()
    return lista

todos_os_alinhamentos = chamar_alinhamento()

#sorteios
sorteando_alinhamentos = choice(todos_os_alinhamentos)
sorteando_habil = choice(todas_as_habil)
sorteando_missoes = choice(todas_as_missoes)
sorteando_fraquezas = choice(todas_as_fraquezas)
sorteando_mundos = choice(todos_os_mundos)
sorteando_armas = choice(todas_as_armas)
sorteando_Classes = choice(todas_as_Classes)
sorteando_racas = choice(todas_as_racas)
#sorteios

#probabilidades
def obter_forca(nivel):
    if nivel <= 5:
        return "Desnutrição extrema.."
    if nivel <= 10:
        return "Fraqueza"
    if nivel <= 25:
        return "Pessoa comum"
    if nivel <= 38:
        return "Média baixa/ força de jovem não acadêmico."
    if nivel <= 50:
        return "Atleta/guerreiro"
    if nivel <= 60:
        return "Touro"
    if nivel <= 70:
        return "Guerreiro Tanque"
    if nivel <= 80:
        return "Pequeno gigante"
    if nivel <= 99:
        return "Titã"
    if nivel <= 200:
        return "Esmagador de montanhas"
    if nivel <= 300:
        return "Sol pequeno"
    if nivel <= 500:
        return "Sistema solar"
    if nivel <= 600:
        return "Galáxia de andrômeda"
    if nivel <= 800:
        return "Multiversal baixo"
    if nivel <= 900:
        return "Multiversal médio"
    if nivel <= 1000:
        return "Grande multiverso"
       
sorteio_forca = randint(1, 1000)
pegarforca = obter_forca(sorteio_forca)

def obter_QI(nivel):
    if nivel <= 50:
        return "Iniciante, apenas medita e sente energia."
    if nivel <= 51:
        return "Fortalece socos e saltos simples, mas ainda aprendiz."
    if nivel <= 140:
        return "Pre-sente ataques, e guia melhor os golpes."
    if nivel <= 200:
        return "Consegue projetar armas de Qi."
    if nivel <= 300:
        return "Mestre, produz rajadas de Qi, e caminha sobre a água."
    if nivel <= 600:
        return "Sábio| Voa e tem uma espécie de telepatia"
    if nivel <= 900:
        return "Ancião| Pode atravessar paredes e acelerar deterioramento de materiais."
    if nivel <= 1000:
        return "Entidade da sabedoria| Manipulação detalhada de tudo ao redor, e força gigante em telepatia."
    if nivel <= 1500:
        return "Oniciente"
    if nivel <= 1800:
        return "Mega oniciencia"

sorteio_Qi = randint(1,1800)
pegarQi = obter_QI(sorteio_Qi)

def obter_agilidade(valor):
    if valor <= 10:
        return "Lesma"
    if valor <= 20:
        return "Criança correndo."
    if valor <= 30:
        return "Pessoa com dor no joelho."
    if valor <= 40:
        return "Humano comum"
    if valor <= 50:
        return "Atleta olímpico"
    if valor <= 60:
        return "Flash"
    if valor <= 70:
        return "Vulto"
    if valor <= 90:
        return "Consegue viajar entre o espaço e o tempo."
    if valor <= 100:
        return "Força de aceleração (flash)"
    if valor <= 200:
        return "onipresença"
    
sorteio_agilidade = randint(1,200)
pegarAgil = obter_agilidade(sorteio_agilidade)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='roleta')
async def roleta(ctx):
    ID_DO_CANAL = 1477809812187119750 
    canal = await bot.fetch_channel(ID_DO_CANAL)
    
    # Sorteios numéricos na hora
    f_num = randint(1, 1000)
    q_num = randint(1, 1800)
    a_num = randint(1, 200)
    
    embed = discord.Embed(title="🎲 Nova Ficha de Personagem", color=discord.Color.blue())
    embed.add_field(name="🧬 Raça", value=choice(chamar_racas()), inline=True)
    embed.add_field(name="👀 Alinhamento", value=choice(chamar_alinhamento()), inline=True)
    embed.add_field(name="💥 Habilidades", value=choice(chamar_habil()), inline=True)
    embed.add_field(name="⚔️ Classe", value=choice(chamar_classes()), inline=True)
    embed.add_field(name="🔫 Armas", value=choice(chamar_armas()), inline=True)
    embed.add_field(name="💀 Fraquezas", value=choice(chamar_fraquezas()), inline=True)
    embed.add_field(name="🌍 Mundo", value=choice(chamar_mundos()), inline=False)
    embed.add_field(name="💪 Força", value=f"{obter_forca(f_num)} ({f_num})", inline=True)
    embed.add_field(name="🧠 QI", value=f"{obter_QI(q_num)} ({q_num})", inline=True)
    embed.add_field(name="🏃 Agilidade", value=f"{obter_agilidade(a_num)} ({a_num})", inline=True)
    embed.add_field(name="🎯 Missão", value=choice(chamar_missao()), inline=False)
    
    # MANDANDO NO CANAL ESPECÍFICO:
    await canal.send(embed=embed)
    # AVISANDO NO CHAT QUE FOI ENVIADO:
    await ctx.send(f"✅ {ctx.author.mention}, sua ficha foi enviada em {canal.mention}!")
# --- WEB SERVER PARA O RENDER (Keep Alive) ---
app = Flask('')
@app.route('/')
def home(): return "Bot está vivo!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- EXECUÇÃO ---
if __name__ == "__main__":
    keep_alive()
    # O Token deve ser colocado nas variáveis de ambiente do Render

    bot.run(os.getenv('DISCORD_TOKEN'))





