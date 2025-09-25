<script setup>
import { ref, onMounted } from 'vue';
import ProductsView from './views/ProductsView.vue';
import LoginView from './views/LoginView.vue';

// Uma variável reativa para controlar o estado de login
const isLoggedIn = ref(false);

// Quando o App é montado, verificamos se existe um token no localStorage
onMounted(() => {
  if (localStorage.getItem('authToken')) {
    isLoggedIn.value = true;
  }
});

// Função de logout
const logout = () => {
  localStorage.removeItem('authToken');
  window.location.reload();
};
</script>

<template>
  <header>
    <h1>Nosso ERP</h1>
    <button v-if="isLoggedIn" @click="logout" class="logout-btn">Logout</button>
  </header>
  <main>
    <ProductsView v-if="isLoggedIn" />
    <LoginView v-else />
  </main>
</template>

<style scoped>
header {
  background-color: #2c3e50;
  color: white;
  padding: 15px 30px;
  text-align: center;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
main {
  padding: 20px;
  background-color: #f4f4f9;
}
.logout-btn {
  background-color: #dc3545;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
}
</style>