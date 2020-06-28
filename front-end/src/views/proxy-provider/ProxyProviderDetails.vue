<template>
    <div>
        <CRow>
            <CCol sm="24" md="12">
                <CCard>
                    <CCardHeader>
                        <h3> Proxy Providers </h3>
                    </CCardHeader>
                    <CCardBody>
                        <CCardHeader>Proxy Address: <strong>{{proxy_providers.proxy_provider_address}}</strong></CCardHeader>
                        <CCardBody>
                            <p>
                                <strong>Last Updated Datetime: </strong> {{proxy_providers.updated_time}}
                            </p>
                            <br>
                            <p>
                                <strong>Total Proxy Found: </strong> {{proxy_providers.new_proxies}}
                            </p>
                            <br>
                            <p>
                                <strong>Next Update Time Interval: </strong> {{proxy_providers.time_interval}}
                            </p>
                            <br>
                            <CDataTable :items="proxies" :fields=table_field
                                        striped
                                        fixed
                                        bordered
                                        pagination
                            >
                            <template #is_test_passed="{item, index}">
                                <td class="py-2">
                                    <div  v-if="Boolean(item.last_test_id)">

                                    <p v-if="Boolean(item.is_test_passed)">
                                            <CBadge color="success">Passed</CBadge>
                                    </p>
                                    <p v-else>
                                        <CBadge color="danger">Failed</CBadge>
                                    </p>
                                    </div>
                                </td>
                            </template>
                            <template #show_details="{item, index}">
                                <td class="py-2">
                                    <CButton v-if="Boolean(item.last_test_id)"
                                            color="success"
                                            square
                                            size="sm"
                                            @click="redirect_url(item, index)"
                                    >
                                       Details
                                    </CButton>
                                </td>
                            </template>
                                <template #header>
                                    <CIcon name="cil-description"/> List of Proxy Service Provider

                                </template>
                            </CDataTable>
                        </CCardBody>
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
            console.log(this.$route.params.id);
            axios.get(`http://localhost:8000/api/proxy-service-provider/${field.$route.params.id}`).then(function(response){
                    field.proxy_providers = response.data.output
                    field.proxies = field.proxy_providers.proxies
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
                proxies: null,
                table_field: ["ip_address", "port_number","last_found", "first_found", "last_successful_functionality_test","is_test_passed", {
                    key: 'show_details',
                    label: 'Last Test Details',
                    _style: 'width:10%',
                    sorter: false,
                    filter: false
                }]
            }
        },
        methods: {
            redirect_url: function (item, index) {
                console.log(index)
                console.log(item)
                this.$router.push({ path: `/functional-details/${item.last_test_id}`})
            }
        }
    }
</script>
