export class LanguageAssessmentService {
  constructor(private readonly API_BASE: string) {}

  /**
   * 启动语言评估
   * @param planId 计划ID
   * @param moduleId 模块ID
   * @param userName 用户名称
   * @returns 评估启动结果（包含record_id和word_list）
   */
  async assessmentStart(planId: number, moduleId: number, userName: string): Promise<{
    success: boolean;
    data: {
      record_id: number;
      word_list: string[];
    }
  }> {
    const response = await fetch(`${this.API_BASE}/language_assessment_start`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ planId, moduleId, userName })
    });
    if (!response.ok) throw new Error('评估启动失败');
    return response.json();
  }

  /**
   * 处理评估步骤1a
   * @param planId 计划ID
   * @param moduleId 模块ID
   * @param recordId 记录ID
   * @param step1aAnswer 步骤1a的答案列表（长度需为40）
   * @returns 步骤1a结果（包含record_id和新的word_list）
   */
  async assessmentStep1a(planId: number, moduleId: number, recordId: number, step1aAnswer: string[]): Promise<{
    success: boolean;
    data: {
      record_id: number;
      word_list: string[];
    }
  }> {
    const response = await fetch(`${this.API_BASE}/language_assessment_step_1a`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ planId, moduleId, recordId, step1aAnswer })
    });
    if (!response.ok) throw new Error('步骤1a处理失败');
    return response.json();
  }

  /**
   * 处理评估步骤1b
   * @param planId 计划ID
   * @param moduleId 模块ID
   * @param recordId 记录ID
   * @param step1bAnswer 步骤1b的答案列表
   * @returns 步骤1b结果（包含record_id和新的word_list）
   */
  async assessmentStep1b(planId: number, moduleId: number, recordId: number, step1bAnswer: string[]): Promise<{
    success: boolean;
    data: {
      record_id: number;
      question_list: any[];
    }
  }> {
    const response = await fetch(`${this.API_BASE}/language_assessment_step_1b`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ planId, moduleId, recordId, step1bAnswer })
    });
    if (!response.ok) throw new Error('步骤1b处理失败');
    return response.json();
  }

  /**
   * 处理评估步骤2
   * @param planId 计划ID
   * @param moduleId 模块ID
   * @param recordId 记录ID
   * @param step2Answer 步骤2的答案列表
   * @returns 最终评估结果
   */
  async assessmentStep2(planId: number, moduleId: number, recordId: number, step2Answer: number[]): Promise<{
    success: boolean;
    data: {
      is_step_2: boolean;
      question_list: any[];
      final_result: string;
    }
  }> {
    const response = await fetch(`${this.API_BASE}/language_assessment_step_2`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ planId, moduleId, recordId, step2Answer })
    });
    if (!response.ok) throw new Error('步骤2处理失败');
    return response.json();
  }
}
