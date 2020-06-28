<template>
    <div>
        <CAlert
                :show.sync="dismissCountDown"
                closeButton
                color="success"
                fade
                :show="alert_success"
        >
            Proxy Provider Information Created Successfully
        </CAlert>
        <CAlert closeButton :show.sync="dismissCountDown" show color="danger" :show="alert_danger">
            <strong>Error Occurred!</strong> When Creating Proxy Provider Information.
            <p>{{ error ? error.message : ""}}</p>
        </CAlert>
        <CRow>
            <CCol sm="24" md="12">
                <CCard>
                    <CCardHeader>
                        <h3> Proxy Providers </h3>
                        <CButton color="success" @click="myModal = true" class="float-right mr-1">
                            Insert a new Proxy Provider
                        </CButton>
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
                        </CCol>
                    </CCardBody>
                </CCard>
            </CCol>
        </CRow>
        <CModal
                title="Create a new Proxy Provider"
                :show.sync="myModal"
                size="xl"
                :close-on-backdrop="false"
        >
            <CCol sm="24">
                <CCard>
                    <CCardHeader>
                        <strong>Proxy Provider Information</strong>
                    </CCardHeader>
                    <CCardBody>
                        <div>
                            <CRow>
                                <CCol md="12">
                                    <CInput
                                            key="proxy_provider_address"
                                            :was-validated="proxy_provider_address.was_validated"
                                            :is-valid="proxy_provider_address.was_validated"
                                            :description="proxy_provider_address.description"
                                            v-model="proxy_provider_address.value"
                                            label="Proxy Provider Address"
                                            placeholder="Enter Proxy Provider Address e.g. https://<proxy_provider_address>"
                                    />
                                </CCol>
                            </CRow>
                            <CInput
                                    key="time_interval"
                                    v-model="time_interval.value"
                                    label="Update Time Interval"
                                    placeholder="Enter Time Interval"
                                    type="number"
                                    min="10"
                                    :was-validated="time_interval.was_validated"
                                    :is-valid="time_interval.was_validated"
                                    :description="time_interval.description"

                            />
                            <CInputCheckbox
                                    v-model="is_https_filtered"
                                    label="Is Https Filtered"
                                    :value="true"
                                    :custom="key > 1"
                                    name="Is Https Filtered"
                            />

                        </div>

                    </CCardBody>
                </CCard>
            </CCol>
            <template #footer>
                <CButton @click="myModal = false" color="danger">Discard</CButton>
                <CButton @click="submitProxyAddress()" color="success">Submit</CButton>
            </template>
        </CModal>
    </div>
</template>



<script>
    import CTableWrapper from '../base/Table.vue'
    window.axios = require('axios')
    export default {
        props: ['proxy_providers_props'],
        name: 'ProxyProviderList',
        components: { CTableWrapper },
        mounted: function(){
            this.updateTableData();
        },
        data: function () {
            return {
                dismissCountDown: 5,
                show: true,
                alert_success: false,
                alert_danger: false,
                isCollapsed: true,
                proxy_providers: this.proxy_providers_props,
                table_field: ["proxy_provider_address", "is_https_filtered", "updated_time", {
                    key: 'show_details',
                    label: '',
                    _style: 'width:1%',
                    sorter: false,
                    filter: false
                },
                ],
                proxy_provider_address: {
                    value: null,
                    description: null,
                    was_validated: null,
                },
                is_https_filtered: false,
                time_interval: {
                    value: null,
                    description: null,
                    was_validated: null,
                },
                success: null,
                error: null,
                myModal: false,

            }
        },
        methods: {
            countDownChanged (dismissCountDown) {
                this.dismiss = dismissCountDown
            },
            updateTableData: function(){
                const field = this
                axios.get('http://localhost:8000/api/proxy-service-provider/list/').then(function(response){
                        field.proxy_providers = response.data.output
                        console.log(response.data.output)
                    }
                ).catch(error => this.proxy_providers = {
                    'error': 'Error Occurred'
                })
            },
            redirect_url: function (item, index) {
                console.log(index)
                console.log(item)
                this.$router.push({ path: `details/${item.id}`})
            },
            submitProxyRequest: function(){
                console.log('GOT')
                console.log(this.proxy_provider_address.value)
                console.log('GOT')
                this.proxy_provider_address.was_validated = false
                this.proxy_provider_address.description = 'Please provide a valid proxy provider address'


            },
            submitProxyAddress: function(){
                const fields = this
                fields.success = null
                fields.error = null

                fields.proxy_provider_address.was_validated = true
                fields.time_interval.was_validated = true
                fields.proxy_provider_address.description = ''
                fields.time_interval.description = ''
                console.log(fields.is_https_filtered)
                axios.post('http://localhost:8000/api/proxy-service-provider/', {
                    data: {
                        proxy_provider_address: fields.proxy_provider_address.value,
                        time_interval: fields.time_interval.value,
                        is_https_filtered: fields.is_https_filtered === false || fields.is_https_filtered === null  ? false : true,

                    }
                }).then(function(response){
                    fields.success = response.data
                    fields.myModal = false
                    fields.alert_success = true;

                    fields.proxy_provider_address.was_validated = null
                    fields.time_interval.was_validated = null
                    fields.proxy_provider_address.description = ''
                    fields.proxy_provider_address.value = ''
                    fields.time_interval.description = ''
                    fields.time_interval.value = ''
                    fields.updateTableData();
                }).catch(function(error){
                    fields.error = error.response.data.message;
                    if(fields.error.hasOwnProperty('proxy_provider_address')){
                        fields.proxy_provider_address.was_validated = false
                        fields.proxy_provider_address.description = 'Please provide a valid proxy provider address'
                    }
                    if(fields.error.hasOwnProperty('time_interval')){
                        fields.time_interval.was_validated = false
                        fields.time_interval.description = 'Please provide a valid time_interval'
                    }
                })


            }

        }
    }
</script>
