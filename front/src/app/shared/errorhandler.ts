export const Handler = {
    handleError(error: any): Promise<any> {
        console.error('An error occurred: ', error);
        return Promise.reject(error.message || error);
    }
};



