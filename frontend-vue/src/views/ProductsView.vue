<script setup>
import { ref } from 'vue';

const username = ref('');
const password = ref('');
const errorMessage = ref(null);

const handleLogin = async () => {
  errorMessage.value = null; // Limpa mensagens de erro antigas
  const loginData = {
    username: username.value,
    password: password.value,
  };

  try {
    const response = await fetch('http://127.0.0.1:8000/api/auth/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(loginData)
    });

    const data = await response.json();

    if (!response.ok) {
      // Pega a mensagem de erro do backend, se houver
      throw new Error(data.non_field_errors || 'Erro ao tentar fazer login.');
    }

    // Se o login for bem-sucedido, salva o token e recarrega a página
    localStorage.setItem('authToken', data.key);
    window.location.reload();

  } catch (error) {
    console.error('Erro de login:', error);
    errorMessage.value = error.message;
  }
};
</script>

<template>
  <div class="login-container">
    <div class="login-box">
      <h2>Login do Sistema</h2>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="username">Usuário:</label>
          <input type="text" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="password">Senha:</label>
          <input type="password" v-model="password" required>
        </div>
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>
        <button type="submit">Entrar</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}
.login-box {
  padding: 40px;
  background: white;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  border-radius: 8px;
  width: 100%;
  max-width: 400px;
}
.error-message {
  color: #dc3545;
  margin-bottom: 15px;
}
</style>