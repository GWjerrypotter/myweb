<template>
  <div>
    <v-nav2></v-nav2>
    <div style="height:1000px"></div>
  </div>
</template>

<script>
import nav2 from "../nav2/2";
export default {
  data() {
    return {};
  },
  components: {
    "v-nav2": nav2
  },
  destroyed() {
    this.reload();
  },
  methods: {
    reload() {
      window.location.reload();
    }
  }
};
</script>

<style scope>
</style>