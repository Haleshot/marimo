/* Copyright 2024 Marimo. All rights reserved. */

import { createReducerAndAtoms } from "@/utils/createReducer";
import type { ColumnPreviewSummary, DatasetsState } from "./types";
import { useAtomValue } from "jotai";
import type { JsonString } from "@/utils/json/base64";

function initialState(): DatasetsState {
  return {
    tables: [],
    expandedTables: new Set(),
    expandedColumns: new Set(),
    columnsPreviews: new Map(),
  };
}

const {
  reducer,
  createActions,
  valueAtom: datasetsAtom,
  useActions,
} = createReducerAndAtoms(initialState, {
  addDatasets: (state, datasets: Pick<DatasetsState, "tables">) => {
    // Put new tables at the top
    const newTables = [...datasets.tables, ...state.tables];
    // Dedupe by name and source
    const seen = new Set();
    const dedupedTables = newTables.filter((table) => {
      const key = `${table.name}:${table.source}`;
      if (seen.has(key)) {
        return false;
      }
      seen.add(key);
      return true;
    });
    return {
      ...state,
      tables: dedupedTables,
    };
  },
  toggleTable: (state, tableName: string) => {
    const expandedTables = new Set(state.expandedTables);
    if (expandedTables.has(tableName)) {
      expandedTables.delete(tableName);
    } else {
      expandedTables.add(tableName);
    }
    return { ...state, expandedTables };
  },
  toggleColumn: (state, opts: { table: string; column: string }) => {
    const tableColumn = `${opts.table}:${opts.column}` as const;
    const expandedColumns = new Set(state.expandedColumns);
    if (expandedColumns.has(tableColumn)) {
      expandedColumns.delete(tableColumn);
    } else {
      expandedColumns.add(tableColumn);
    }
    return { ...state, expandedColumns };
  },
  addColumnPreview: (
    state,
    opts: {
      table: string;
      column: string;
      chart_spec?: JsonString;
      error?: string;
      summary?: ColumnPreviewSummary;
    },
  ) => {
    const tableColumn = `${opts.table}:${opts.column}` as const;
    const columnsPreviews = new Map(state.columnsPreviews);
    columnsPreviews.set(tableColumn, {
      chart_spec: opts.chart_spec,
      error: opts.error,
      summary: opts.summary,
    });
    return { ...state, columnsPreviews };
  },
});

/**
 * React hook to get the datasets state.
 */
export const useDatasets = () => useAtomValue(datasetsAtom);

/**
 * React hook to get the datasets actions.
 */
export function useDatasetsActions() {
  return useActions();
}

export const exportedForTesting = {
  reducer,
  createActions,
  initialState,
};
