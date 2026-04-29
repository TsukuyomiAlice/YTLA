export interface ScaffoldModuleRequest {
  isCore: boolean;
  typeName: string;
  structure: string;
  subTypeName: string;
  genBackend: boolean;
  genFrontend: boolean;
}

export interface ScaffoldModuleResponse {
  success: boolean;
  message: string;
  results: {
    backend: string | null;
    frontend: string | null;
  };
}

export class ScaffoldModuleService {
  constructor(private readonly API_BASE: string) {}

  async generateScaffold(request: ScaffoldModuleRequest): Promise<{
    success: boolean;
    data: ScaffoldModuleResponse;
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
