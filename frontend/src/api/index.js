// import Vue from 'vue'
import axios from 'axios'
import Urls from '@/api/urls'

function createAxiosInstance(baseUrl, timeOut) {
  const axiosInstance = axios.create({
    baseURL: baseUrl,
    timeout: timeOut,
  })
  return axiosInstance
}

// function setInterceptors(instance) {
//   instance.interceptors.request.use(function (config) {
//     const accessToken = localStorage.getItem("access_token");
//     if (accessToken) {
//       config.headers["Authorization"] = `Bearer ${accessToken}`;
//     }
//     return config;
//   });

//   instance.interceptors.response.use(
//     function (response) {
//       return response;
//     },
//     function (error) {
//       // Vue.$log.error('!intercept error!', error)
//       // Vue.$log.error('status : ', error.response.status)
//       // Vue.$log.error('message : ', error.response.data.message)
//       return Promise.reject(error);
//     }
//   );

//   return instance;
// }

const myAxios = createAxiosInstance(Urls.Django_API, 1000)

export default myAxios
