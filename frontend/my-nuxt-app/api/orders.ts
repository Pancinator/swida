import type { TransportOrder, PaginatedResponse } from '~/interfaces/TransportOrderTypes'
// @ts-ignore
import { useRuntimeConfig } from '#app'

class ApiService {
  private baseApi: string;

  constructor(apiBase: string) {
    this.baseApi = apiBase;
    console.log("ApiService initialized with baseApi:", this.baseApi); // Debug log
  }

  async getOrders(queryParams: Record<string, string> = {}): Promise<TransportOrder[]> {
    console.log("Fetching orders from:", `${this.baseApi}/orders/`); // Debug log
    const data = await $fetch<PaginatedResponse<TransportOrder>>(`${this.baseApi}/orders/`, {
      query: queryParams
    });
    return data.results;
  }
  
  async getOrderById(id: string): Promise<TransportOrder> {
    return $fetch(`${this.baseApi}/orders/${id}`);
  }
  
  async createOrder(orderData: TransportOrder): Promise<TransportOrder> {
    return $fetch(`${this.baseApi}/orders/create/`, {
      method: 'POST',
      body: orderData
    });
  }
  
  async deleteOrder(id: string): Promise<void> {
    return $fetch(`${this.baseApi}/orders/${id}/`, {
      method: 'DELETE'
    });
  }
}

// ✅ **Factory function to create an instance of ApiService**
export function createApiServiceFactory() {
  const { public: config } = useRuntimeConfig();
  console.log("Creating ApiService with base URL:", config.backendURL); // Debug log
  return new ApiService(config.backendURL);
}
