# 🎶 Spotify Top 5 Tracks 🎶

Este repositório é uma adaptação em Python do código fornecido pelo [Spotify Developers](https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks) que retorna o top 5 músicas mais ouvidas do usuário.

## 📑 Pré-requisitos
- Requests
- Spotipy
- Aplicação criada no site [Spotify for Developers > Dashboard](https://developer.spotify.com/)

## 🖥️ Instalação

1. Clone o repositório em sua máquina local:

    ```
    git clone https://github.com/laribalera/spotify_top_5
    ```

## 🖥️ Uso

Faz um request GET no endpoint `v1/me/top/tracks?time_range=long_term&limit=5` e itera sobre a resposta retornando o nome do artista e a música. É possivel alterar o limit para retornar mais músicas e também o range de tempo.

## 🆗 Atualizações

- [x] Criar front end 

## 🛠️ TO-DO

- [ ] Adicionar opções de configuração para a chamada (mudar range e limit)
- [ ] Melhorar template
- [ ] Configurar autenticação
