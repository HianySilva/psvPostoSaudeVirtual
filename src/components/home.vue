<template>
  <div class="container">
    <div class="cabecalho-logo">
      <header class="cabecalho">
        <img class="logo" src="../assets/my-logo.png">
        <span><strong>Posto de Saúde Virtual</strong></span>
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
              <li class="nav-item">
                <a class="nav-link disabled" aria-current="page" href="#" id="first-menu">Início</a>
              </li>
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
                <a class="nav-link active" aria-current="page" href="loginPage" id="first-menu">Login</a>
              </li>
            </ul>
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="cadastroPage" id="first-menu">Cadastrar</a>
              </li>
            </ul>    
          </div>
        </div>
      </nav>
    </div>
    <div class="corpo-img">
      <img src="../assets/body-picture.png" id="body-picture">
    </div>
    <div class="row">
      <div class="col-3">
        <div class="card" style="width: 12rem;">
          <img src="../assets/agendamentoConsulta.png">
        </div>
      </div>
      <div class="col-3">
        <div class="card" style="width: 12rem;">
          <img src="../assets/visualizarExames.png">
        </div>
      </div>
      <div class="col-3">
        <div class="card" style="width: 12rem;">
          <img src="../assets/atendimentoVirtual.png">
        </div>
      </div>
      <div class="col-3">
        <div class="card" style="width: 12rem;">
          <img src="../assets/medicamentosDisponiveis.png">
        </div>
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
  name: 'homePage',
  props: {
    msg: String
  }
}
</script>

<style scoped>
.container {
  height: 100vh;
}
.cabecalho {
  width: 20vw;
  color: #051775;
  font-size: 15pt;
}
.logo {
  width: 5vw;
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
.corpo-img{
  margin-top: 0.5em;
}
#body-picture {
  width: 100%;
  height: 35vh;
}
.row {
  margin-top: 0.5em;
}
.card {
  margin-left: 3.5em;
}
.rodape {
  background-color: #051775;
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