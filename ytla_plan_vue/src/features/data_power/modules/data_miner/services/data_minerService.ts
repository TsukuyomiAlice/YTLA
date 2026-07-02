export class Data_minerService {
  constructor(private readonly API_BASE: string) {}

  /**
   * 获取原始数据文件列表
   * @param planId 计划ID
   */
  async getSourceFiles(planId: number): Promise<{
    success: boolean
    files?: Array<{
      file_name: string
      file_path: string
      file_size: number
      upload_time: string
      module_id: number
      module_name: string
      file_type: string
    }>
    message?: string
  }> {
    const response = await fetch(`${this.API_BASE}/data_miner/source_files?plan_id=${planId}`, {
      method: 'GET',
    })
    if (!response.ok) throw new Error('获取原始文件列表失败')
    return response.json()
  }

  /**
   * 获取已处理数据文件列表
   * @param planId 计划ID
   * @param moduleId 模组ID（可选），若提供则只返回该模组的文件
   */
  async getProcessedFiles(planId: number, moduleId?: number): Promise<{
    success: boolean
    files?: Array<{
      file_name: string
      file_path: string
      file_size: number
      processed_time: string
      module_id: number
      module_name: string
      output_format: string
      source_file: string
    }>
    message?: string
  }> {
    let url = `${this.API_BASE}/data_miner/processed_files?plan_id=${planId}`
    if (moduleId !== undefined) {
      url += `&module_id=${moduleId}`
    }
    const response = await fetch(url, { method: 'GET' })
    if (!response.ok) throw new Error('获取已处理文件列表失败')
    return response.json()
  }

  /**
   * 分析处理原始文件
   * @param planId 计划ID
   * @param sourceFilePath 原始文件路径
   * @param moduleId 模组ID
   */
  async processFile(planId: number, sourceFilePath: string, moduleId: number): Promise<{
    success: boolean
    data?: any
    message?: string
    error?: string
  }> {
    const response = await fetch(`${this.API_BASE}/data_miner/process`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ plan_id: planId, source_file_path: sourceFilePath, module_id: moduleId }),
    })
    if (!response.ok) throw new Error('文件分析失败')
    return response.json()
  }

  /**
   * 查看已处理文件内容
   * @param planId 计划ID
   * @param filePath 文件路径
   */
  async viewProcessedFile(planId: number, filePath: string): Promise<{
    success: boolean
    data?: any
    content?: any
    message?: string
  }> {
    const response = await fetch(`${this.API_BASE}/data_miner/view?plan_id=${planId}&file_path=${encodeURIComponent(filePath)}`, {
      method: 'GET',
    })
    if (!response.ok) throw new Error('查看文件失败')
    return response.json()
  }

  /**
   * 删除已处理文件
   * @param planId 计划ID
   * @param filePath 文件路径
   */
  async deleteProcessedFile(planId: number, filePath: string): Promise<{
    success: boolean
    message?: string
    error?: string
  }> {
    const response = await fetch(`${this.API_BASE}/data_miner/delete`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ plan_id: planId, file_path: filePath }),
    })
    if (!response.ok) throw new Error('删除文件失败')
    return response.json()
  }
}
