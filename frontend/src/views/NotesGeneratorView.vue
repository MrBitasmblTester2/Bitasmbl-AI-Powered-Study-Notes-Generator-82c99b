<template>
  <div class="p-6 max-w-4xl mx-auto">
    <textarea class="w-full border p-3" v-model="text"></textarea>
    <button class="mt-4 px-4 py-2 bg-blue-600 text-white" @click="generate">Generate</button>
    <div v-if="notes" class="mt-6">
      <h2 class="text-xl font-semibold">Summary</h2>
      <p>{{ notes.summary }}</p>
      <h3 class="mt-4 font-semibold">Keywords</h3>
      <ul><li v-for="k in notes.keywords" :key="k">{{ k }}</li></ul>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue'

const text = ref('')
const notes = ref(null)

async function generate() {
  notes.value = null
}
</script>