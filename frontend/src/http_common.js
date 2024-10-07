import axios from 'axios'
import {URI} from './app_constants'
const VAPI = axios.create({
    baseURL: URI,
    timeout: 60000,
  })

  VAPI.defaults.withCredentials = true;

  VAPI.interceptors.request.use(function(config) {
    return config
  })
  
  VAPI.defaults.headers = {
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Expires': '0',
  };
  
export default VAPI