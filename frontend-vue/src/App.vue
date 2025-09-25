<script setup>
import ProductsView from './views/ProductsView.vue';
</script>

<template>
  <header>
    <h1>Nosso ERP</h1>
  </header>
  <main>
    <ProductsView />
  </main>
</template>

<style>
body { margin: 0; font-family: sans-serif; background-color: #f4f4f9; color: #333; }
header { background-color: #2c3e50; color: white; padding: 15px; text-align: center; }
main { padding: 20px; }
</style>