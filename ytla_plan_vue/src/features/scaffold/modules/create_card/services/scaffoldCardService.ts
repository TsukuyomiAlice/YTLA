export interface ScaffoldCardRequest {
  isCore: boolean;
  typeName: string;
  structure: string;
  subTypeName: string;
  genBackend: boolean;
  genFrontend: boolean;
}

export interface ScaffoldCardResponse {
  success: boolean;
  message: string;
  results: {
    backend: string | null;
    frontend: string | null;
  };
}

export class ScaffoldCardService {
  constructor(private readonly API_BASE: string) {}

  async generateScaffold(request: ScaffoldCardRequest): Promise<{
    success: boolean;
    data: ScaffoldCardResponse;
  }> {
    const response = await fetch(`${this.API_BASE}/scaffold/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        is_core: request.isCore,
        type_name: request.typeName,
        structure: request.structure,
        sub_type_name: request.subTypeName,
        gen_backend: request.genBackend,
        gen_frontend: request.genFrontend
      })
    });
    if (!response.ok) throw new Error('脚手架生成失败');
    return response.json();
  }
}
