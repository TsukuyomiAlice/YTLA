export class LanguageDictionaryService {
  constructor(private readonly API_BASE: string) {}

  /**
   * 搜索词典单词
   * @param word 要搜索的单词
   * @returns 搜索结果（包含success状态和data数据）
   */
  async searchWord(word: string): Promise<{
    success: boolean;
    data: {
      meaning: string;
    }
  }> {
    const response = await fetch(`${this.API_BASE}/language_dictionary_search_word`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ word })
    });
    if (!response.ok) throw new Error('词典搜索失败');
    return response.json();
  }
}
