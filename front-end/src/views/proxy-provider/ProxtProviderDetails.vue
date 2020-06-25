<template>
    <div>
        <CRow>
            <CCol sm="24" md="12">
                <CCard>
                    <CCardHeader>
                        <h3> Proxy Providers </h3>
                    </CCardHeader>
                    <CCardBody>

                    </CCardBody>
                </CCard>
            </CCol>
        </CRow>
    </div>
</template>


<script>
    import CTableWrapper from '../base/Table.vue'
    window.axios = require('axios')
    export default {
        name: 'ProxyProviderDetails',
        components: { CTableWrapper },
        mounted: function(){
            const field = this
            axios.get('http://localhost:8000/api/proxy-service-provider/'+'24'+'/details').then(function(response){
                    field.proxy_providers = response.data.output
                    console.log(response.data.output)
                }
            ).catch(error => this.proxy_providers = {
                'error': 'Error Occurred'
            })
        },
        data: function () {
            return {
                show: true,
                isCollapsed: true,
                proxy_providers: null,
                table_field: ["proxy_provider_address", "is_https_filtered", "updated_time", {
                    key: 'show_details',
                    label: '',
                    _style: 'width:1%',
                    sorter: false,
                    filter: false
                }]

            }
        }
    }
</script>
