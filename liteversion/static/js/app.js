const App = {
   data():{
   return{
   like: 0,
   dislike: 0

   }
      },
   delimiters: ["${", "}$"],

      methods:{
      addLike(){
      this.like +=1;
      },
      addDisLike(){
      this.dislike +=1;
      },
      }
}

Vue.createApp(App, {delimiters: ['${', '}$']}).mount("#app")
