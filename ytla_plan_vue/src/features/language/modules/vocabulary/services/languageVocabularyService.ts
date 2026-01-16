export class LanguageVocabularyService {
  constructor(private readonly API_BASE: string) {}

  /**
   * 创建新词汇本
   * @param planId 计划ID
   * @param moduleId 模块ID
   * @param userName 用户名称
   * @param wordList 初始单词列表
   */
  async createNewVocabularyBook(planId: number, moduleId: number, userName: string, wordList: string[] = []): Promise<{
    success: boolean;
    data?: {
      record_id: number;
    }
  }> {
    const response = await fetch(`${this.API_BASE}/language_vocabulary_new`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ planId, moduleId, userName, wordList })
    });
    if (!response.ok) throw new Error('创建词汇本失败');
    return response.json();
  }

  /**
   * 获取用户所有词汇本
   * @param planId 计划ID
   * @param moduleId 模块ID
   * @param userName 用户名称
   */
  async getAllVocabularies(planId: number, moduleId: number, userName: string): Promise<{
    success: boolean;
    data: {
      records: {
        record_id: number;
        vocabulary_book_name: string;
        word_list: string[];
      }[];
    }
  }> {
    const response = await fetch(`${this.API_BASE}/language_vocabulary_get_all`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ planId, moduleId, userName })
    });
    if (!response.ok) throw new Error('获取词汇本失败');
    return response.json();
  }

  /**
   * 更新词汇本单词列表
   * @param planId 计划ID
   * @param moduleId 模块ID
   * @param recordId 记录ID
   * @param wordList 新的单词列表
   */
  async updateWordList(planId: number, moduleId: number, recordId: number, wordList: string[]): Promise<{
    success: boolean;
  }> {
    const response = await fetch(`${this.API_BASE}/language_vocabulary_update_word_list`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ planId, moduleId, record_id: recordId, word_list: wordList })
    });
    if (!response.ok) throw new Error('更新单词列表失败');
    return response.json();
  }

  /**
   * 更新词汇本名称
   * @param planId 计划ID
   * @param moduleId 模块ID
   * @param recordId 记录ID
   * @param bookName 新书名
   */
  async updateBookName(planId: number, moduleId: number, recordId: number, bookName: string): Promise<{
    success: boolean;
  }> {
    const response = await fetch(`${this.API_BASE}/language_vocabulary_update_book_name`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ planId, moduleId, record_id: recordId, book_name: bookName })
    });
    if (!response.ok) throw new Error('更新书名失败');
    return response.json();
  }
}
