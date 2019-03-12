import request from '@/utils/request'

export function getBrief() {
  return request({
    url: '/doc/',
    method: 'get',
  })
}