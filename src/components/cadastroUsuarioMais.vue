<template>
  <div class="container">
    <div class="cabecalho-logo">
      <header class="cabecalho">
        <img class="logo" src="../assets/my-logo.png">
        <span><strong>Posto de Saúde Virtual</strong></span>
      </header>
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
                <a class="nav-link active" aria-current="page" href="agendarConsulta" id="second-menu"><strong>Agendar Consulta</strong></a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-current="page" href="#" id="seta"><i class="fa-solid fa-chevron-right"></i></a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-current="page" href="#" id="second-menu"><strong>Casdastrar</strong></a>
              </li>
            </ul>  
          </div>  
        </div>  
      </nav>  
    </div>
    <div class="atendente">
      <header class="header-atendente">
        <img class="atendente-img" src="../assets/atendente.png">
        <span><strong id="atendente-voice">Cadastro neste site<i class="fa-solid fa-volume-high" id="sound"></i></strong></span>
      </header>
    </div>
    <div id="body-cadastro">
      <form class="card">
        <div class="card-header">
          <svg xmlns="http://www.w3.org/2000/svg" width="75" height="75" fill="white"  class="bi bi-person-circle" viewBox="0 0 16 16">
            <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
            <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
          </svg>
        </div>
        <div class="card-content">
          <div class="card-content-area">
            <label for="sus">Nº do Cartão do SUS</label>
            <input type="text" name="cartaoSus" id="sus" autocomplete="off" v-model="NºdoCartãodoSUS">
          </div>
          <div class="card-content-area">
            <label for="cpf">CPF</label>
            <input type="text" name="cpf" id="cpf" autocomplete="off" v-model="CPF">
          </div>
          <div class="card-content-area">
            <label for="data">Data de Nascimento</label>
            <input type="date" name="data" id="data" autocomplete="off" v-model="DatadeNascimento">
          </div>
          <div class="card-content-area">
            <label for="phone">Telefone</label>
            <input type="tel" name="phone" id="phone" pattern="\([0-9]{2}\)[9]{1}[0-9]{4}-[0-9]{4}" placeholder="(xx)9xxxx-xxxx" autocomplete="off" v-model="Telefone">
          </div>
          <div class="card-content-area">
            <label for="rua">Rua</label>
            <input type="text" name="rua" id="rua" autocomplete="off" v-model="Rua">
          </div>
          <div class="card-content-area">
            <label for="cep">CEP</label>
            <input type="text" name="cep" id="cep" autocomplete="off" v-model="CEP">
          </div>
          <div class="card-content-area">
            <label for="numero">Número</label>
            <input type="text" name="numero" id="numero" autocomplete="off" v-model="Número">
          </div>
          <div class="card-content-area">
            <label for="bairro">Bairro</label>
            <input type="text" name="bairro" id="bairro" autocomplete="off" v-model="Bairro">
          </div>
          <div class="card-content-area">
            <label for="complemento">Complemento</label>
            <input type="text" name="complemento" id="complemento" autocomplete="off" v-model="Complemento">
          </div>
          <div class="card-content-area">
            <label for="referencia">Referência</label>
            <input type="text" name="referencia" id="referencia" utocomplete="off" v-model="Referência">
            <span v-show="deuErro1" class="erro-senha"
              ><i class="fa fa-times"></i>Nenhum dado cadastrado ou Dados
              incopletos</span
            >
          </div>
        </div>
        <div class="card-footer">
          <button
            v-on:click="Cadastrar()"
            class="btn col-2"
          >
            CADASTRAR
          </button>
        </div>
        <div class="voltar">
            <router-link to= "agendarConsulta"><img class="seta" src="../assets/seta.png"></router-link>
        </div>  
      </form>  
    </div>  
  </div>
</template>

<script>
export default {
  name: "cadastroUsuarioMais",
  data() {
    return {
      deuErro1: false,
      deuErro: false,
      NºdoCartãodoSUS: '',
      CPF: '',
      DatadeNascimento: '',
      Telefone: '',
      Rua: '',
      CEP: '',
      Número: '',
      Bairro: '',
      Complemento: '',
      Referência: '',
    };
  },
  methods: {
    Cadastrar() {
        if (
        this.NºdoCartãodoSUS == "" ||
        this.NºdoCartãodoSUS == " " ||
        this.NºdoCartãodoSUS < 3 ||
        this.CPF == "" ||
        this.CPF == " " ||
        this.CPF < 3 ||
        this.Rua == "" ||
        this.Rua == " " ||
        this.Rua < 3 ||
        this.CEP == "" ||
        this.CEP == " " ||
        this.CEP < 3 ||
        this.Bairro == "" ||
        this.Bairro == " " ||
        this.Bairro < 3 ||
        this.Complemento == "" ||
        this.Complemento == " " ||
        this.Complemento < 3 ||
        this.Referência == "" ||
        this.Referência == " " ||
        this.Referência < 3 ||
        this.DatadeNascimento == "" ||
        this.Telefone == "" ||
        this.Número == ""
      ) {
        this.deuErro1 = true;
        this.NºdoCartãodoSUS = "";
        this.CPF = "";
        this.DatadeNascimento = "";
        this.Telefone = "";
        this.Rua = "";
        this.CEP = "";
        this.Número = "";
        this.Bairro = "";
        this.Complemento = "";
        this.Referência = "";
      } else {
          this.$router.push("agendarConsulta");
        }
    } 
  },
};
</script>

<style scoped>
.container {
  height: 195vh;
}
.cabecalho {
  width: 20vw;
  color: #ffffff;
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
  background-color: #051775;
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
.atendente-img {
  height: 10vh;
  border-radius: 100%;

}
#atendente-voice {
  background-color: #051775;
  color: #ffffff;
  border-radius: 50px 50px 50px 50px;
}
#sound {
  margin: 0.5em;
}
 #body-cadastro {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 101vh;
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}
.card {
  background-color: #051775;
  position: absolute;
  top: 30%;
  padding: 8%;
  border-radius: 2px;
  border-radius: 50px 50px 50px 50px;
  width: 70vw;
  height: 165vh;
}
.card-header{
  position: absolute;
  top:2%;
  background: none;
  left: 45%;
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
.card-footer .submit{
  position:absolute;
  width: 15%;
  right: 10%;
  height: 40px;
  background-color: #66C4F9;
  border-radius: 10px 10px 10px 10px;
  border:none;
  color: #ffffff;
  margin: 10px 0;
}
.card-footer a {
  text-align: center;
  font-size: 12px;
  opacity: 0.8;
  color: #ffffff;
  text-decoration: none;
}
.rede{
  color:white;
}
.iconeRedes{
  width: 5%;
}
.btn {
  background-color: #66C4F9;
  border-radius: 50px 50px 50px 50px;
  margin: 0.5em;
  margin-left: 86%;
  width: 8vw;
}
.seta {
  width: 5%;
  border-radius: 80px 80px 80px 80px;
}
</style>