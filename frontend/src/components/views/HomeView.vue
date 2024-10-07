<template>
    <div class="home">
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">{{$t('inventory.name')}}</th>
                    <th scope="col">{{$t('inventory.quantity')}}</th>
                    <th scope="col">{{$t('inventory.price')}}</th>
                    <th scope="col">{{$t('inventory.supplier')}}</th>
                    <th scope="col">{{$t('inventory.action')}}</th>
                  </tr>
            </thead>
            <tbody>
                <tr scope="row" v-for="(product, index) in products" :key="index">
                  <td >{{product.name}}</td>
                  <td >{{product.quantity}}</td>
                  <td >{{product.price}}</td>
                  <td >{{product.supplier}}</td>
                  <td>
                    <b-button @click="$router.push({name: 'product', params: {idProduct: product.id_product}})">
                        {{$t('inventory.edit')}}
                    </b-button> 
                    <b-button @click="deleteProduct(product.id_product)" variant="secondary">
                        {{$t('inventory.delete')}}
                    </b-button>
                  </td>
                </tr>
            </tbody>
        </table>

    </div>
</template>

<script>
import VAPI from '@/http_common';
import { HTTP_STATUS, SERVICE_NAMES } from "@/app_constants";
export default {
    name: 'HomeView',
    data() {
      return {
        products: [],
      };
    },
    mounted() {
        this.getAllProducts();
    },
    methods: {
        async getAllProducts() {
            try {
                let response = await VAPI.get(`${SERVICE_NAMES.INVENTORY}/get-all`)
                if(response.status == HTTP_STATUS.OK){
                    this.products = response.data
                }
            } catch (error) {
                console.error(error)
            }
        },
        deleteProduct(idProduct){
            console.log(idProduct)
            // TODO
        }
    },
}
</script>

<style lang="scss" scoped>
    
</style>
