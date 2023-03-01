import myAxios from '@/api/AxiosInstanceController'
import urls from '@/api/urls'

export default {
  async fetchWordsearch(postData) {
    const response = await myAxios
      .post(urls.wordsearch_all, postData)
      .then(() => {
        // store.commit("userStore/dialogOpen", "login");
      })
      .catch((error) => {
        console.log(error.response)
      })
    return response
  },

  getMyDetail() {
    myAxios
      .get(urls.users_Me)
      .then((response) => {
        // store.commit("userStore/loginSuccess", response.data);
      })
      .catch((error) => {
        console.log('getMyDetail GET error', error.response)
      })
  },
}
