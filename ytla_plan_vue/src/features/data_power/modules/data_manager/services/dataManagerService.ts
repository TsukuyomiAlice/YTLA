export class DataManagerService {
  constructor(private readonly API_BASE: string) {}

  /**
   * 获取文件列表
   * @param planId 计划ID
   */
  async getFiles(planId: number): Promise<{
    success: boolean
    files?: Array<{
      file_name: string
      file_path: string
      file_size: number
      upload_time: string
      module_id: number
      module_name: string
      module_subtype_name: string
    }>
    message?: string
  }> {
    const response = await fetch(`${this.API_BASE}/data_manager/files?plan_id=${planId}`, {
      method: 'GET',
    })
    if (!response.ok) throw new Error('获取文件列表失败')
    return response.json()
  }

  /**
   * 上传文件
   * @param file 文件对象
   * @param moduleId 模块ID
   */
  async uploadFile(file: File, moduleId: number): Promise<{
    success: boolean
    file_info?: {
      file_name: string
      file_path: string
      file_size: number
      upload_time: string
    }
    error?: string
  }> {
    const formData = new FormData()
    formData.append('file', file)
    formData.append('module_id', String(moduleId))

    const response = await fetch(`${this.API_BASE}/data_manager/upload`, {
      method: 'POST',
      body: formData,
    })
    if (!response.ok) throw new Error('上传文件失败')
    return response.json()
  }

  /**
   * 删除文件
   * @param filePath 文件路径
   */
  async deleteFile(filePath: string): Promise<{
    success: boolean
    message?: string
    error?: string
  }> {
    const response = await fetch(`${this.API_BASE}/data_manager/files/delete`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ file_path: filePath }),
    })
    if (!response.ok) throw new Error('删除文件失败')
    return response.json()
  }
}
