<template>
  <div class="container">
    <div class="cabecalho-logo">
      <header class="cabecalho">
        <img class="logo" src="../assets/agendamentoConsulta.png">
        <span><strong>Agendar Consulta</strong></span>
      </header>
    </div>
    <div class="menu">
      <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
          <a class="navbar-brand" href="#"><i class="fa-solid fa-bars" id="icon-nav"></i></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Médicos
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Dra. Izabella Tabosa</a></li>
                  <li><a class="dropdown-item" href="#">Dr. Fabrício Torres</a></li>
                  <li><a class="dropdown-item" href="#">Dr. Luiz Alberto</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Ver mais...</a></li>
                </ul>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Serviços
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Pré Natal</a></li>
                  <li><a class="dropdown-item" href="#">Aplicações de Vacinas</a></li>
                  <li><a class="dropdown-item" href="#">Prevenção na saúde da mulher</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Ver mais...</a></li>
                </ul>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Postos
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Zenobio de Melo</a></li>
                  <li><a class="dropdown-item" href="#">Santa Rosa</a></li>
                  <li><a class="dropdown-item" href="#">Santa Luzia</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Ver mais...</a></li>
                </ul>
              </li>
            </ul>
            <form class="d-flex">
              <input class="form-control me-2" type="search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit"><i class="fa-solid fa-magnifying-glass"></i></button>
            </form>
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="cadastroUsuarioMais" id="first-menu">Iniciar Cadastro</a>
              </li>
            </ul>
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="#" id="first-menu">Excluir Cadastro</a>
              </li>
            </ul>    
          </div>
        </div>
      </nav>
    </div>
    <div class="next-page">
      <nav class="navbar navbar-expand-lg next-page">
        <div class="container-fluid">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="funcionalidadesPage" id="second-menu"><strong>Todas as funcionalidades</strong></a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-current="page" href="#" id="seta"><i class="fa-solid fa-chevron-right"></i></a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-current="page" href="#" id="second-menu"><strong>Agendar consulta</strong></a>
              </li>
            </ul>  
          </div>  
        </div>  
      </nav>  
    </div>
    <div class="new-next-page">
      <nav class="navbar navbar-expand-lg next-page">
        <div class="container-fluid">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="agendarConsulta" id="second-menu"><strong>Passo 1</strong></a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-current="page" href="#" id="seta"><i class="fa-solid fa-chevron-right"></i></a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-current="page" href="#" id="second-menu"><strong>Passo 2</strong></a>
              </li>
            </ul>  
          </div>  
        </div>  
      </nav>  
    </div>
    <div class="atendente">
        <header class="header-atendente">
            <img class="atendente-img" src="../assets/atendente.png">
            <span><strong id="atendente-voice">Preenchar os dados a seguir para concluir o seu agendamento de consulta<i class="fa-solid fa-volume-high" id="sound"></i></strong></span>
        </header>
    </div>
    <div class="botao">
        <button type="button" class="btn" id="mensagem">Sicronize suas informações do SUS no nosso site<i class="fa-solid fa-arrows-spin" id="spinner"></i></button>
    </div>
    <div id="body-cadastro">
        <form class="card">
            <div class="card-content">
                <div class="card-content-area">
                    <label for="posto">Postos</label>
                    <input type="text" id="posto" autocomplete="off" v-model="Postos">
                </div>
                <div class="card-content-area">
                    <label for="data">Data</label>
                    <input type="date" id="data" autocomplete="off" v-model="Data">
                </div>
                <div class="card-content-area">
                    <label for="hora">Hora</label>
                    <input type="time" id="hora" autocomplete="off" v-model="Hora">
                    <span v-show="deuErro1" class="erro-senha"
                    ><i class="fa fa-times"></i>Nenhum dado cadastrado ou Dados
                    incopletos</span
                    >
                    <span v-show="deuErro" class="erro-senha"
                    ><i class="fa fa-times"></i>As senhas digitadas não conferem</span
                    >
                </div>
            </div>    
        </form>
        <div class="botao">
            <button v-on:click="Confirmar()" type="button" class="btn" id="confirmar">Confirmar</button>
        </div>
    </div>    

    <div class="rodape">
      <footer class="rodape-footer">
        <div class="row">
          <div class="col-4">
            <div class="contatos">
              <h5>Contatos:</h5>
              <h5><i class="fa-solid fa-envelope"></i>posto.saúdevirtual27palmares@gmail.com</h5>
              <h5><i class="fa-solid fa-phone"></i>(81) 98349-6015</h5>
            </div>
          </div>
          <div class="col-4">
            <div class="contatos">
              <h5>Conheça-nos</h5>
              <h5><i class="fa-solid fa-location-dot"></i>Palmares, Cep: 55540-000</h5>
            </div>
          </div>
          <div class="col-4">
            <div class="contatos">
              <h5>Redes Sociais:</h5>
              <i class="fa-brands fa-instagram" id="instagram"></i><i class="fa-brands fa-twitter" id="twitter"></i><i class="fa-brands fa-facebook"></i>
            </div>
          </div>
        </div>
      </footer>
  </div>
  </div>
</template>

<script>
export default {
  name: "agPasso2",
  data() {
    return {
      deuErro1: false,
      deuErro: false,
      Postos: "",
      Data: "",
      Hora: "",
    };
  },
  methods: {
    Confirmar() {
      if (
        this.Postos == "" ||
        this.Postos == " " ||
        this.Postos < 3
      ) {
        this.deuErro1 = true;
        this.Postos = "";
        this.Data = "";
        this.Hora = "";
      } else {
          this.$router.push("agendarConsulta");
        }
    },
  },
}
</script>

<style scoped>
.cabecalho {
  width: 20vw;
  color: #051775;
  font-size: 15pt;
}
.logo {
  width: 5vw;
  border-radius: 100%;
}
strong {
  margin-left: 0.5em;
}
.cabecalho-logo {
  margin-top: 0.5em;
}
.menu {
  margin-top: 0.5em;
}
.navbar {
  background-color: #051775;
}
#icon-nav {
  color: #ffffff;
}
#first-menu {
  color: #ffffff;
  
}
#navbarDropdown  {
  color: #ffffff;
}
.d-flex {
  margin-right: 10%;
}
input {
  background: none;
  height: 5vh;
  width: 30vw;
  border-radius: 7px 7px 7px 7px;
}
.btn {
  background: none;
  color: #ffffff;
}
.next-page {
  background-color: #ffffff;
}
#second-menu {
  color: #051775;
}
#seta {
  color: #66C4F9
}
.new-next-page {
  background-color: #ffffff;
  margin-left: 7%;
}
.atendente-img {
  height: 10vh;
  border-radius: 100%;

}
#atendente-voice {
  background-color: #051775;
  color: #ffffff;
}
#sound {
  margin: 0.5em;
}
.rodape {
  background-color: #051775;
  margin-top: 0.5em;
}
.contatos {
  color: #ffffff;
  text-align: center;
}
#instagram {
  margin-right: 15%;
}
#twitter {
  margin-right: 15%;
}
#mensagem {
    background-color: #66C4F9;
    color: #ffffff;
    margin-left: 69%;
}
#spinner {
    margin: 0.5em;
}
.card {
  background-color: #051775;
  margin: 0.5em;
  margin-left: 25%;
  padding: 5%;
  border-radius: 20px 20px 20px 20px;
  width: 40vw;
  height: 60vh;
}
.card-content label {
  color: #ffffff;
  font-size: 18pt;
  opacity: 0.8;
}
.card-content-area {
  display: flex;
  flex-direction: column;
  padding:10px 0;
}
.card-content-area input {
  margin-top: 10px;
  padding:0 5px;
  background-color: transparent;
  border:none;
  border-bottom: 1px solid #ffffff;
  outline: none;
  color: #ffffff;
}
#confirmar {
    background-color: #66C4F9;
    color: #ffffff;
    margin-left: 93%;
}
</style>