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
                <a class="nav-link disabled" aria-current="page" href="#" id="second-menu"><strong>Passo 1</strong></a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-current="page" href="#" id="seta"><i class="fa-solid fa-chevron-right"></i></a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="agPasso2" id="second-menu"><strong>Passo 2</strong></a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-current="page" href="#" id="seta"><i class="fa-solid fa-chevron-right"></i></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="#" id="second-menu"><strong>Passo 3</strong></a>
              </li>
            </ul>  
          </div>  
        </div>  
      </nav>  
    </div>
    <div class="row">
        <div class="col-6">
            <div class="atendente">
                <header class="header-atendente">
                    <img class="atendente-img" src="../assets/atendente.png">
                    <span><strong id="atendente-voice">Atenção: Necessita de consulta domiciliar?<i class="fa-solid fa-volume-high" id="sound"></i></strong></span>
                    <form id="dados">
                        <input type="radio" name="pergunta" id="pergunta-sim" value="sim">
                        <label for="pergunta-sim"><strong class="resposta">Sim</strong></label>
                        <input type="radio" name="pergunta" id="pergunta-nao" value="não">
                        <label for="pergunta-nao"><strong class="resposta">Não</strong></label>
                    </form>
                </header>
            </div>
            <div class="atendente">
                <header class="header-atendente-second">
                    <img class="atendente-img" src="../assets/atendente.png">
                    <span><strong id="atendente-voice">Escolha a melhor data para você agendar sua consulta?<i class="fa-solid fa-volume-high" id="sound"></i></strong></span>
                </header>    
            </div>
            <div class="body-dados">
                <form action="#" class="dados">
                    <div class="row">
                        <div class="col-6">
                            <input type="checkbox" name="consulta1" id="consulta1" value="Consulta Médica">
                            <label for="consulta1">Consulta Médica</label>
                        </div>
                        <div class="col-6">
                            <input type="checkbox" name="consulta2" id="consulta2" value="Consulta ao Dentista">
                            <label for="consulta1">Consulta ao Dentista</label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-6">
                            <input type="checkbox" name="consulta3" id="consulta3" value="Atendimento Virtual">
                            <label for="consulta3">Atendimento Virtual</label>
                        </div>
                        <div class="col-6">
                            <input type="checkbox" name="consulta4" id="consulta4" value="Atendimento a Domicílio">
                            <label for="consulta4">Atendimento a Domicílio</label>
                        </div>
                    </div>
                </form>    
            </div>
            <div class="body-dados-second">
                <div class="row">
                    <div class="col-6">
                        <form action="#" class="dados-second">
                            <div class="row">
                                <div class="col-12">
                                    <i class="fa-solid fa-clock"></i>Manhã
                                </div>
                                <div class="row">
                                    <div class="col-4">
                                        <label class="horas">8:20</label>
                                    </div>
                                    <div class="col-4">
                                        <label class="horas">9:20</label>
                                    </div>
                                    <div class="col-4">
                                        <label class="horas">10:20</label>
                                    </div>
                                    <div class="row">
                                        <div class="col-4">
                                            <label class="horas">08:40</label>
                                        </div>
                                        <div class="col-4">
                                            <label class="horas">09:40</label>
                                        </div>
                                        <div class="col-4">
                                            <label class="horas">10:40</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </form>    
                    </div>
                    <div class="col-6">
                        <form action="#" class="dados-second">
                            <div class="row">
                                <div class="col-12">
                                    <i class="fa-solid fa-clock"></i>Tarde
                                </div>
                                <div class="row">
                                    <div class="col-4">
                                        <label class="horas">14:00</label>
                                    </div>
                                    <div class="col-4">
                                        <label class="horas">15:00</label>
                                    </div>
                                    <div class="col-4">
                                        <label class="horas">16:00</label>
                                    </div>
                                    <div class="row">
                                        <div class="col-4">
                                            <label class="horas">14:40</label>
                                        </div>
                                        <div class="col-4">
                                            <label class="horas">15:40</label>
                                        </div>
                                        <div class="col-4">
                                            <label class="horas">16:40</label>
                                        </div>
                                        <div class="row">
                                            <div class="col-12">
                                                <label class="horas">17:00</label>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </form>    
                    </div>
                </div>    
            </div>
        </div>
        <div class="col-6">

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
  name: 'agendarConsulta',
  props: {
    msg: String
  }
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
#dados {
    background-color: #051775;
    height: 10vh;
    width: 28vw;
    margin-left: 10%;
}
#pergunta-sim {
    margin-top: 4%;
    margin-left: -30%;
    margin-right: -50%;
}
#pergunta-nao {
    margin-top: 4%;
    margin-left: -30%;
    margin-right: -50%;
}
.resposta {
    color: #ffffff;
    font-size: 15pt;
}
.header-atendente-second {
    margin-top: 3%;
    margin-left: 16%;
}
.dados {
    width: 100%;
    margin-top: 2%;
    margin-left: 16%;
    background-color: #051775;
    color: #ffffff;
    text-align: center;
    font-size: 15pt;
    height: 25vh;
    padding-top: 3%;
    border-radius: 20px 20px 20px 20px;
}
.dados-second {
    width: 100%;
    margin-top: 3%;
    margin-left: 35%;
    background-color: #051775;
    color: #ffffff;
    text-align: center;
    font-size: 15pt;
    height: 27vh;
    padding-top: 3%;
    border-radius: 20px 20px 20px 20px;
}
.horas {
    padding-top: 1em;
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
</style>