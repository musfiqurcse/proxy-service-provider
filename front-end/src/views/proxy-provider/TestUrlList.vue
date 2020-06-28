<template>
    <div>
       <CAlert
              :show.sync="dismissCountDown"
              closeButton
              color="success"
              fade
              :show="alert_success"
            >
             Test URL Created Successfully
            </CAlert>
        <CAlert closeButton show color="danger" :show="alert_danger">
            <strong>Error!</strong> When Creating Test URL.
            <p>{{ error ? error.message : ""}}</p>
        </CAlert>
        <CRow>
            <CCol sm="24" md="12">
                <CCard>
                    <CCardHeader>
                        <h3> Test URL </h3>
                        <CButton color="success" @click="myModal = true" class="float-right mr-1">
                            Insert a new Test URL
                        </CButton>
                    </CCardHeader>
                    <CCardBody>
                        <CCol lg="12">
                            <CDataTable :items="test_urls" :fields=table_field
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
                                    <CIcon name="cil-description"/> List of Test URL

                                </template>
                            </CDataTable>
                        </CCol>
                    </CCardBody>
                </CCard>
            </CCol>
        </CRow>
        <CModal
                title="Create a new Test URL"
                :show.sync="myModal"
                size="xl"
                :close-on-backdrop="false"
        >
            <CCol sm="24">
                <CCard>
                    <CCardHeader>
                        <strong>Test URL Information</strong>
                    </CCardHeader>
                    <CCardBody>
                        <div>
                            <CRow>
                                <CCol md="12">
                                    <CInput
                                            :was-validated="test_url_provider_name.was_validated"
                                            :is-valid="test_url_provider_name.was_validated"
                                            :description="test_url_provider_name.description"
                                            v-model="test_url_provider_name.value"
                                            label="TEST URL Provider Name"
                                            placeholder=""
                                    />
                                </CCol>
                            </CRow>
                            <CInput
                                    v-model="test_url_address.value"
                                    label="Test URL Address"
                                    placeholder="Enter Test URL Address e.g. https://<test-url-address>"
                                    min="10"
                                    :was-validated="test_url_address.was_validated"
                                    :is-valid="test_url_address.was_validated"
                                    :description="test_url_address.description"

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
        props: ['test_urls_props'],
        name: 'TestUrlList',
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
                test_urls: this.test_urls_props,
                table_field: ["test_url_provider_name", "test_url_address", "updated_time"
                ],
                test_url_address: {
                    value: null,
                    description: null,
                    was_validated: null,
                },
                test_url_provider_name: {
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
            axios.get('http://localhost:8000/api/test-url/list/').then(function(response){
                    field.test_urls = response.data.output
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
            submitProxyAddress: function(){
              const fields = this
              fields.success = null
              fields.error = null
              axios.post('http://localhost:8000/api/test-url/', {
                  data: {
                     test_url_provider_name: fields.test_url_provider_name.value,
                     test_url_address: fields.test_url_address.value

                  }
              }).then(function(response){
                    fields.success = response.data
                    fields.myModal = false
                    fields.updateTableData();
              }).catch(function(response){
                  fields.error = response.data
              })

            }

        }
    }
</script>
