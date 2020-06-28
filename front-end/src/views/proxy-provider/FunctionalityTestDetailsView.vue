<template>
    <div>
        <CRow>
            <CCol sm="24" md="12">
                <CCard>
                    <CCardHeader>
                        <h3> Functionality Test Details </h3>
                    </CCardHeader>
                    <CCardBody>
                        <CCardHeader>Test URL Address: <strong>{{func_test.test_url_address}}</strong></CCardHeader>
                        <CCardBody>
                            <p>
                                <strong>Test Perform Time: </strong> {{func_test.created_time}}
                            </p>
                            <br>
                            <p>
                                <strong>Proxy IP Address </strong> {{func_test.ip_address}}
                            </p>
                            <br>
                            <p>
                                <strong>Proxy Port Number </strong> {{func_test.port_number}}
                            </p>
                            <br>

                            <p v-if="Boolean(func_test.is_test_passed)">
                                <strong>Test Status </strong> <CBadge color="success">Passed</CBadge>
                            </p>
                            <p v-else>
                                <strong>Test Status </strong> <CBadge color="danger">Failed</CBadge>
                            </p>
                            <br>
                            <p>
                                <strong>Test Output Message </strong> {{func_test.test_mesasge}}
                            </p>
                            <br>
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
        name: 'FunctionalityTestDetailsView',
        components: { CTableWrapper },
        mounted: function(){
            const field = this
            console.log(this.$route.params.id);
            axios.get(`http://localhost:8000/api/functional-test/${field.$route.params.id}`).then(function(response){
                    field.func_test = response.data.output
                }
            ).catch(error => this.proxy_providers = {
                'error': 'Error Occurred'
            })
        },
        data: function () {
            return {
                show: true,
                isCollapsed: true,
                func_test: null,
                proxies: null,

            }
        },
        methods: {
            redirect_url: function (item, index) {
                console.log(index)
                console.log(item)
                this.$router.push({ path: `details/${item.id}`})
            }
        }
    }
</script>
