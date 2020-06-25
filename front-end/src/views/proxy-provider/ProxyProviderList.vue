<template>
    <div>
        <CRow>
         <CCol sm="24" md="12">
        <CCard>
          <CCardHeader>
            List of Proxy Providers
            <div class="card-header-actions">
              <a
                href="https://coreui.io/vue/docs/components/card-components"
                class="card-header-action"
                rel="noreferrer noopener"
                target="_blank"
              >
                <small class="text-muted">docs</small>
              </a>
            </div>
          </CCardHeader>
          <CCardBody>
            {{loremIpsum}}
          </CCardBody>
        </CCard>
      </CCol>
<!--            <CCol sm="6" md="4">-->
<!--        <CCard>-->
<!--          <CCardBody>{{loremIpsum}}</CCardBody>-->
<!--          <CCardFooter>Card Footer</CCardFooter>-->
<!--        </CCard>-->
<!--      </CCol>-->
<!--      <CCol sm="6" md="4">-->
<!--        <CCard>-->
<!--          <CCardHeader><CIcon name="cil-check"/> Card with icon</CCardHeader>-->
<!--          <CCardBody>{{loremIpsum}}</CCardBody>-->
<!--        </CCard>-->
<!--      </CCol>-->
<!--      <CCol sm="6" md="4">-->
<!--        <CCard>-->
<!--          <CCardHeader>-->
<!--            Card with switch-->
<!--            <CSwitch-->
<!--              class="float-right"-->
<!--              size="sm"-->
<!--              shape="pill"-->
<!--              color="info"-->
<!--              data-on="On"-->
<!--              data-off="Off"-->
<!--              :checked="true"-->
<!--            />-->
<!--          </CCardHeader>-->
<!--          <CCardBody>-->
<!--            {{loremIpsum}}-->
<!--          </CCardBody>-->
<!--        </CCard>-->
<!--      </CCol>-->
<!--      <CCol sm="6" md="4">-->
<!--        <CCard>-->
<!--          <CCardHeader>-->
<!--            Card with label-->
<!--            <CBadge color="success" class="float-right">Success</CBadge>-->
<!--          </CCardHeader>-->
<!--          <CCardBody>-->
<!--            {{loremIpsum}}-->
<!--          </CCardBody>-->
<!--        </CCard>-->
<!--      </CCol>-->
<!--      <CCol sm="6" md="4">-->
<!--        <CCard>-->
<!--          <CCardHeader>-->
<!--            Card with label-->
<!--            <CBadge shape="pill" color="danger" class="float-right">42</CBadge>-->
<!--          </CCardHeader>-->
<!--          <CCardBody>-->
<!--            {{loremIpsum}}-->
<!--          </CCardBody>-->
<!--        </CCard>-->
<!--      </CCol>-->
    </CRow>
    </div>
</template>



<script>

export default {
  name: 'ProxyProviderList',
  data: function () {
    return {
      show: true,
      isCollapsed: true,
      loremIpsum: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.'
    }
  }
}
</script>
