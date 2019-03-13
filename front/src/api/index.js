import request from '@/utils/request'

export function getnewsBrief() {
  return request({
    url: '/doc/?page_size=1000',
    method: 'get',
  })
}