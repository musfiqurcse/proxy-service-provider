<template>
    <div>
        <CRow>
            <CCol sm="24" md="12">
                <CCard>
                    <CCardHeader>
                        <h3> Proxy Providers </h3>
                    </CCardHeader>
                    <CCardBody>
                        <CCardHeader>
                            <h5>Proxy Address: <strong>{{proxy_providers.proxy_provider_address}}</strong>
                                <CButton color="success" @click="updateModal = true" class="float-md-right mr-1">
                                    Update Proxy List
                                </CButton>
                                <CButton color="primary" @click="testModal = true" class="float-md-right mr-1">
                                    Perform Functional Test
                                </CButton>
                            </h5>


                        </CCardHeader>
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
                            <p>
                                <strong>Functional Proxy Test Session: </strong>
                                 <CBadge v-if="proxy_providers.functionality_test_state === 'not_running'" color="primary">NOT RUNNING</CBadge>
                                <CBadge v-if="proxy_providers.functionality_test_state === 'completed'"  color="success">COMPLETED</CBadge>
                                 <CBadge v-if="proxy_providers.functionality_test_state === 'running'"  color="warning">RUNNING</CBadge>
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
        <CModal
                title="Update Proxy List"
                :show.sync="updateModal"
                size="xl"
                :close-on-backdrop="false"
        >
            <CCol sm="24">
                <CCard>
                    <CCardHeader>
                        <strong>Update Proxy List</strong>
                    </CCardHeader>
                    <CCardBody>
                        <div>
                            <CRow>
                                <CCol md="12">
                                    <p>Proxy Address: <strong>{{proxy_providers.proxy_provider_address}}</strong></p>
                                </CCol>
                                <CCol md="12">
                                    <p>
                                        <strong>Last Updated Datetime: </strong> {{proxy_providers.updated_time}}
                                    </p>
                                </CCol>
                                <CCol md="12">
                                    <p>
                                        <strong>Next Update Time Interval: </strong> {{proxy_providers.time_interval}}
                                    </p>
                                </CCol>

                                <CCol md="12">
                                    <h5 class="text-success">
                                        Do you want to update the Proxy List of this Proxy Proxy Provider
                                    </h5>
                                    <h5 class="text-danger">
                                        {{updateProxyError}}
                                    </h5>
                                </CCol>
                            </CRow>
                        </div>

                    </CCardBody>
                </CCard>
            </CCol>
            <template #footer>
                <CButton @click="closeUpdateModal()" color="danger">Cancel</CButton>
                <CButton @click="confirmUpdate()" color="success">Confirm Update!</CButton>
            </template>
        </CModal>
        <CModal
                title="Perform Functional Test"
                :show.sync="testModal"
                size="xl"
                :close-on-backdrop="false"
        >
            <CCol sm="24">
                <CCard>
                    <CCardHeader>
                        <strong>Perform Functional Test</strong>
                    </CCardHeader>
                    <CCardBody>
                        <CRow>
                            <CCol class="md-12">
                                <CSelect v-model="testURLSelected"
                                    label="Test URL"
                                    size="lg"
                                    horizontal
                                    :options="selectTestOptions"
                                    placeholder="Please select a Test URL"
                                  />
                            </CCol>
                        </CRow>
                        <CRow>

                            <CCol class="md-12">
                                <h5 class="text-danger">
                                        {{testURLModelError}}
                                </h5>
                            </CCol>
                        </CRow>
                    </CCardBody>
                </CCard>
            </CCol>
            <template #footer>
                <CButton @click="closeTestURLModal()" color="danger">Discard</CButton>
                <CButton @click="performTest()" color="success">Perform Test</CButton>
            </template>
        </CModal>
    </div>
</template>


<script>
    import CTableWrapper from '../base/Table.vue'
    window.axios = require('axios')
    export default {

        props: ['proxy_details_props','proxies_props'],
        name: 'ProxyProviderDetails',
        components: { CTableWrapper },
        mounted: function(){
            this.updateDetailsTable();
            this.getTestURLData();
        },
        data: function () {
            return {
                show: true,
                testURLSelected: null,
                isCollapsed: true,
                proxy_providers: this.proxy_details_props,
                proxies: this.proxies_props,
                updateModal: false,
                testModal: false,
                testURLData: null,
                testURLModelError: "",
                updateProxyError: "",
                selectTestOptions: [],
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
            },
            getTestURLData: function(){
                const field = this
                axios.get('http://localhost:8000/api/test-url/list/').then(function(response){
                        field.testURLData = response.data.output
                        let options = []
                        for(var i=0; i< field.testURLData.length; i+=1){
                            let item = {
                                value: field.testURLData[i].id,
                                label: field.testURLData[i].test_url_address,
                            }
                            options.push(item)
                        }
                        field.selectTestOptions = options;
                    }
                ).catch(function(error){
                    fields.testURLData = error.response.data.message
                })
            },
            updateDetailsTable: function(){
                const field = this
                console.log(this.$route.params.id);
                axios.get(`http://localhost:8000/api/proxy-service-provider/${field.$route.params.id}`).then(function(response){
                        field.proxy_providers = response.data.output
                        field.proxies = response.data.output.proxies
                        console.log(response.data.output)
                    }
                ).catch(error => this.proxy_providers = {
                    'error': 'Error Occurred'
                })
            },
            confirmUpdate: function(){
                const fields = this
                axios.put(`http://localhost:8000/api/proxy-service-provider/${fields.$route.params.id}/update-proxy/`, {
                    data: {
                        proxy_provider_address: fields.proxy_providers.proxy_provider_address,
                        time_interval: fields.proxy_providers.time_interval,
                        is_https_filtered: fields.proxy_providers.is_https_filtered === false? false: true,

                    }
                }).then(function(response){
                    fields.success = response.data
                    fields.updateModal = false
                    fields.updateDetailsTable();
                }).catch(function(error){
                    fields.updateProxyError = error.response.data.message
                })
            },
            closeUpdateModal: function(){
                this.updateModal = false
                this.updateProxyError = ""
            },
            performTest: function(){
                const field = this
                console.log(this.$route.params.id);
                console.log(field.testURLSelected.target.value)
                axios.put(`http://localhost:8000/api/proxy-service-provider/${field.$route.params.id}/test/`, {
                    data: {
                        test_url_id: parseInt(field.testURLSelected.target.value)
                    }
                }).then(function(response){
                        field.proxy_providers = response.data.output
                        field.testModal = false
                }).catch(function(error){
                    field.testURLModelError = error.response.data.message;
                })
            },
            closeTestURLModal: function(){
                this.testURLModelError = "";
                this.testModal  = false;
            }
        }
    }
</script>
