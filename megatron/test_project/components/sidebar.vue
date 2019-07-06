<template>
    <div>
      <transition name="slide">
        <aside v-show="isShown">
          <div class="container">
            <button v-if="isLoggedIn">Profile</button>
            <button v-if="isLoggedIn">My Posts</button>
            <button v-if="isLoggedIn">Log Out</button>
            <button v-if="!isLoggedIn">Log In</button>
            <button v-if="!isLoggedIn">Sign In</button>
            <button>About</button>
          </div>
        </aside>
      </transition>
    </div>
</template>

<script>
    export default {
        name: "sidebar",

        props: {
          isShown: {
            type: Boolean,
            default: true,
          },
          isLoggedIn: {
            type: Boolean,
            default: true
          }
        },
    }
</script>

<style scoped>

  aside {
    background-color: #fff;
    width: 350px;
    position: fixed;
    top: 55px;
    left: 0;
    bottom: 0;
    z-index: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
    background-color: rgba(30,144,255, 0.2);
  }

  .container {
    margin-top: 76px;
    display: block;
    width: 100%;
  }

  .container button {
    display: block;
    cursor: pointer;
    width: 100%;
    height: 75px;
    background-color: dodgerblue;
    border: 1px solid blue; /* Green border */
    color: white; /* White text */
    padding: 10px 24px; /* Some padding */
  }

  .container button:not(:last-child) {
    border-bottom: none; /* Prevent double borders */
  }

  .container button:hover {
    background-color: rgba(30,144,255, 0.5);
  }

  aside h2{
    font-weight: 300;
    color: #afafaf;
  }

  * {
    box-sizing: border-box;
  }

  .slide-enter-active, .slide-leave-active {
    transition: all .3s cubic-bezier(.65, .05, .36, 1);
  }

  .slide-enter, .slide-leave-active {
    left: -100%;
  }
</style>
