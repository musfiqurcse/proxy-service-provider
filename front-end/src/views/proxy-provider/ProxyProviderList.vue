<template>
    <div>
        <CRow>
            <CCol sm="24" md="12">
                <CCard>
                    <CCardHeader>
                        <h3> Proxy Providers </h3>
                    </CCardHeader>
                    <CCardBody>
                        <CCol lg="12">
                            <CDataTable :items="proxy_providers" :fields=table_field
                                        striped
                                        fixed
                                        bordered
                            >
                            <template #show_details="{item, index}">
                                <td class="py-2">
                                    <CButton
                                            color="success"
                                            square
                                            size="sm"
                                            @click="toggleDetails(item, index)"
                                    >
                                        Details
                                    </CButton>
                                </td>
                            </template>
                                <template #header>
                                    <CIcon name="cil-description"/> List of Proxy Service Provider

                                </template>
                            </CDataTable>
                        </CCol>
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
        name: 'ProxyProviderList',
        components: { CTableWrapper },
        mounted: function(){
            const field = this
            axios.get('http://localhost:8000/api/proxy-service-provider/list/').then(function(response){
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
