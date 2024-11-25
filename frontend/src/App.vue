<script setup>
import MyForm from './components/MyForm.vue';
</script>

<template>
  <div>
    <MyForm />
  </div>
</template>

<style>
@import "vue-select/dist/vue-select.css";
</style>

<script>
export default {
  components: {
    MyForm
  }
};
</script>