<template>
  <div>
    <div class="header">
      <div class="header-left">
        <button @click="showOrHideSidebar()" class="LogoButton">PostOnline</button>
      </div>
      <div class="header-right">
        <button @click="goTo('/')">Home</button>
        <button @click="goTo('/new')" v-if="isLoggedIn" class="active">New Post</button>
      </div>
    </div>
    <sidebar :is-logged-in="isLoggedIn" :is-shown="isSidebarShown"/>
  </div>
</template>

<script>
  import Sidebar from "../components/sidebar";

  export default {
    name: "AppHeader",

    components: {
      Sidebar,
    },

    data() {
      return {
        isSidebarShown: false,
      }
    },

    methods: {
      goTo(link){
        this.$router.push({path: link})
      },

      showOrHideSidebar()
      {
        this.isSidebarShown = !this.isSidebarShown;
      }
    },

    props: {
      isLoggedIn: {
        type: Boolean,
        default: false,
      }
    },
  }
</script>

<style scoped>
  /* Style the header with a grey background and some padding */
  .header {
    width:100%;
    position: fixed;
    top: 0;
    left: 0;
    font-size: 30px;
    z-index: 80;
    background-color: #fff;
    box-shadow: 2px 2px 5px 0 rgba(0,0,0,0.095);
    padding: 8px 16px;
    box-sizing: border-box;
    overflow: auto;
  }

  /* Float the text section to the right */
  div.header-left {
    float: left;
  }

  /* Float the link section to the right */
  .header-right {
    float: right;
  }

  .link {
    text-decoration: none;
    color: black;
  }

  /* Style the header buttons */
  .header button {
    float: left;
    background: transparent;
    text-align: center;
    padding: 12px;
    font-size: 18px;
    line-height: 25px;
    border-radius: 4px;
    cursor: pointer;
    outline: none;
    border: 0;
    transition: all .3s ease-in-out;
    margin-left: 5px;
  }

  /* Change the background color on mouse-over */
  .header button:hover {
    background-color: #ddd;
    color: black;
  }

  /* Style the active/current link button*/
  .header button.active {
    background-color: dodgerblue;
    color: white;
  }

  .header button.LogoButton {
    font-size: 25px;
  }
</style>
